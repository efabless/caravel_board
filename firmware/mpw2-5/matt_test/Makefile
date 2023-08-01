
TOOLCHAIN_PATH=/usr/local/bin/
#TOOLCHAIN_PATH=/opt/riscv32imc/bin/
# TOOLCHAIN_PATH=/ef/apps/bin/

# Set the prefix for `riscvXX-unknown-elf-*`
# On installations using `multilib`, this will be `riscv64` even for compiling to 32-bit targets
TOOLCHAIN_PREFIX=riscv64
#TOOLCHAIN_PREFIX=riscv32
INCLUDES=-I$(shell pwd) -I../ -I../generated/

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = freq_test pwm_test

hex:  ${PATTERN:=.hex}

gpio_config_data.c: gpio_config_def.py gpio_config_io.py
	python3 ../gpio_config/gpio_config_builder.py

sim: gpio_config_def.py gpio_config_io.py gpio_config_data.c
	python3 ../gpio_config/gpio_config_simulator.py

check: gpio_config_def.py gpio_config_io.py gpio_config_data.c
	python3 ../gpio_config/gpio_config_checker.py

%.elf: %.c ../sections.lds ../crt0_vex.S gpio_config_data.c
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc $(INCLUDES) -O0 -mabi=ilp32 -march=rv32i_zicsr -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c $<
	${TOOLCHAIN_PATH}$(TOOLCHAIN_PREFIX)-unknown-elf-objdump -D $@ > $*.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O verilog $< $@
	sed -i '.orig' -e 's/@1000/@0000/g' $@

%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: freq_test.hex
	python3 ../util/caravel_hkflash.py freq_test.hex
	python3 ../util/caravel_hkstop.py

flash_pwm: pwm_test.hex
	python3 ../util/caravel_hkflash.py pwm_test.hex
	python3 ../util/caravel_hkstop.py

flash_nucleo: freq_test.hex
	make -f ../nucleo/Makefile flash FILE=freq_test.hex

flash_nucleo_pwm: pwm_test.hex
	make -f ../nucleo/Makefile flash FILE=pwm_test.hex

sanity_check: gpio_config_def.py
	make -f ../nucleo/Makefile sanity_check FILE=gpio_config_def.py

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.lst *.orig gpio_config_data.*

.PHONY: clean hex all flash

