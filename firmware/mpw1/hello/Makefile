# Set compilation variables
include ../../environment.mk

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = hello

hex:  ${PATTERN:=.hex}

#%.elf: %.c ../sections.lds ../start.s spi_io.c spi_io.h ../print_io.c ../print_io.h
%.elf: %.c ../sections.lds ../start.s ../print_io.c ../print_io.h
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc -O0 -march=$(TARGET_ARCH) -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../start.s ../print_io.c $<
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objdump -D hello.elf > hello.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O verilog $< $@
	sed -i '.orig' -e 's/@10000000/@00000000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O binary $< $@

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

