
TOOLCHAIN_PATH=/usr/local/bin/
#TOOLCHAIN_PATH=/opt/riscv32imc/bin/
#TOOLCHAIN_PATH=/ef/apps/bin/
#TOOLCHAIN_PATH=/usr/bin/

# Set the prefix for `riscvXX-unknown-elf-*`
# On installations using `multilib`, this will be `riscv64` even for compiling to 32-bit targets
TOOLCHAIN_PREFIX=riscv64
#TOOLCHAIN_PREFIX=riscv32
INCLUDES=-I$(shell pwd) -I../ -I../generated/

VOLTAGE=$(shell python3 -c "from gpio_config_def import voltage; print(voltage)")

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = gpio_test

hex:  ${PATTERN:=.hex}

gpio_config_data.c: gpio_config_def.py gpio_config_io.py
	python3 ../gpio_config/gpio_config_builder.py

sim: gpio_config_def.py gpio_config_io.py gpio_config_data.c
	python3 ../gpio_config/gpio_config_simulator.py

check: gpio_config_def.py gpio_config_io.py gpio_config_data.c
	python3 ../gpio_config/gpio_config_checker.py

%.elf: %.c ../sections.lds ../crt0_vex.S gpio_config_data.c
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc $(INCLUDES) -O0 -mabi=ilp32 -march=rv32i -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c $<
	${TOOLCHAIN_PATH}$(TOOLCHAIN_PREFIX)-unknown-elf-objdump -D $@ > $*.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O verilog $< $@
	sed -i.orig -e 's/@1000/@0000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: gpio_test.hex
	python3 ../util/caravel_hkflash.py $<
	python3 ../util/caravel_hkstop.py

flash_nucleo: gpio_test.hex
	make -f ../nucleo/Makefile flash FILE=gpio_test.hex VOLTAGE=$(VOLTAGE)

sanity_check: gpio_config_def.py
	make -f ../nucleo/Makefile sanity_check FILE=gpio_config_def.py

# run to bringup Caravel power while mounted on Nucleo
poweron:
	make -f ../nucleo/Makefile poweron VOLTAGE=$(VOLTAGE)

change_power:
	make -f ../nucleo/Makefile change_power VOLTAGE=$(VOLTAGE)

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.lst *.orig gpio_config_data.*

.PHONY: clean hex all flash

