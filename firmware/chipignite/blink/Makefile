# Set compilation variables
include ../../environment.mk

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = blink

hex:  ${PATTERN:=.hex}

%.elf: %.c ../sections.lds ../crt0_vex.S
	#$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc -O0 -march=$(TARGET_ARCH) -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../start.s ../print_io.c $<
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=$(TARGET_ARCH) -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c ../stub.c $<
	${TOOLCHAIN_PATH}$(TOOLCHAIN_PREFIX)-unknown-elf-objdump -D blink.elf > blink.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-objcopy -O verilog $< $@
	sed -ie 's/@1000/@0000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: blink.hex
	python3 ../util/caravel_hkflash.py blink.hex

flash2: blink.hex
	python3 ../util/caravel_flash.py blink.hex

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd

.PHONY: clean hex all flash

