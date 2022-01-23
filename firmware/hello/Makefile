TOOLCHAIN_PATH = /opt/riscv32imc/bin/
# TOOLCHAIN_PATH = /ef/apps/bin/

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = hello

hex:  ${PATTERN:=.hex}

%.elf: %.c ../sections.lds ../start.s
	$(TOOLCHAIN_PATH)riscv32-unknown-elf-gcc -O0 -march=rv32i -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../start.s $<
	${TOOLCHAIN_PATH}/riscv32-unknown-elf-objdump -D hello.elf > hello.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)riscv32-unknown-elf-objcopy -O verilog $< $@
	sed -i '.orig' -e 's/@10000000/@00000000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)riscv32-unknown-elf-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: hello.hex
	python3 ../util/caravel_hkflash.py hello.hex

flash2: hello.hex
	python3 ../util/caravel_flash.py $<

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd

.PHONY: clean hex all flash

