TOOLCHAIN_PATH = $(TOOLS)/rv32/bin/
# TOOLCHAIN_PATH = /ef/apps/bin/

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = blink

hex:  ${PATTERN:=.hex}

%.elf: %.c ../sections.lds ../start.s
	$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-gcc -O0 -march=rv32imafdc -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../start.s $<

%.hex: %.elf
	$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-objcopy -O verilog $< $@
	sed -i 's/@10000000/@00000000/g' $@
	$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-objdump -D $< > blink.list

%.bin: %.elf
	$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: blink.hex
	python3 ../util/caravel_hkflash.py blink.hex

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd

.PHONY:  hex all flash

