# Set compilation variables
include ../../environment.mk

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = bitbang

hex:  ${PATTERN:=.hex}

%.elf: %.c ../sections.lds ../crt0_vex.S
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=$(TARGET_ARCH) -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c $<
	${TOOLCHAIN_PATH}$(TOOLCHAIN_PREFIX)-unknown-elf-objdump -D bitbang.elf > bitbang.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O verilog $< $@
	sed -i '.orig' -e 's/@10000000/@00000000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: bitbang.hex
	python3 ../util/caravel_hkflash.py bitbang.hex

flash2: bitbang.hex
	python3 ../util/caravel_flash.py bitbang.hex

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd

.PHONY: clean hex all flash

