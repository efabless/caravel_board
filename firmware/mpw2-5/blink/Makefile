
TOOLCHAIN_PATH=/usr/local/bin/
#TOOLCHAIN_PATH=/opt/riscv32imc/bin/
# TOOLCHAIN_PATH=/ef/apps/bin/

# Set the prefix for `riscvXX-unknown-elf-*`
# On installations using `multilib`, this will be `riscv64` even for compiling to 32-bit targets
TOOLCHAIN_PREFIX=riscv64
#TOOLCHAIN_PREFIX=riscv32

VOLTAGE?=$(shell python3 -c "from gpio_config_def import voltage; print(voltage)")

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = blink

hex:  ${PATTERN:=.hex}

%.elf: %.c ../sections.lds ../crt0_vex.S
	#$(TOOLCHAIN_PATH)riscv32-unknown-elf-gcc -O0 -march=rv32i_zicsr -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../start.s ../print_io.c $<
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=rv32i_zicsr -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c $<
	${TOOLCHAIN_PATH}$(TOOLCHAIN_PREFIX)-unknown-elf-objdump -D blink.elf > blink.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O verilog $< $@
	sed -i '.orig' -e 's/@1000/@0000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: blink.hex
	python3 ../util/caravel_hkflash.py blink.hex

flash2: blink.hex
	python3 ../util/caravel_flash.py blink.hex

flash_nucleo: blink.hex
	make -f ../nucleo/Makefile flash FILE=blink.hex VOLTAGE=$(VOLTAGE)

sanity_check: gpio_config_def.py
	make -f ../nucleo/Makefile sanity_check FILE=gpio_config_def.py

# run to bringup Caravel power while mounted on Nucleo
poweron:
	make -f ../nucleo/Makefile poweron VOLTAGE=$(VOLTAGE)

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd

.PHONY: clean hex all flash

