
TOOLCHAIN_PATH=/foss/tools/riscv-gnu-toolchain-rv32i/217e7f3debe424d61374d31e33a091a630535937/bin/
#TOOLCHAIN_PATH=/opt/riscv32imc/bin/
# TOOLCHAIN_PATH=/ef/apps/bin/

# Set the prefix for `riscvXX-unknown-elf-*`
# On installations using `multilib`, this will be `riscv64` even for compiling to 32-bit targets
TOOLCHAIN_PREFIX=riscv64
#TOOLCHAIN_PREFIX=riscv32

# ---- Test patterns for project raven ----

.SUFFIXES:

PATTERN = config_io_o_h

hex:  ${PATTERN:=.hex}

../gpio_config/gpio_config_data.c: ../gpio_config/gpio_config_def.py
	cd ../gpio_config; python3 ../gpio_config/gpio_config_builder.py

%.elf: %.c ../sections.lds ../crt0_vex.S ../gpio_config/gpio_config_data.c
	$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=rv32i -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c ../gpio_program.c $<

	#$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=rv32i -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c ../gpio_program.c $<
	${TOOLCHAIN_PATH}riscv32-unknown-linux-gnu-objdump -s  config_io_o_h.elf > config_io_o_h.lst

%.hex: %.elf
	$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-objcopy -O verilog $< $@
	sed -ie 's/@10/@00/g' $@
	
%.bin: %.elf
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-objcopy -O binary $< $@

client: client.c
	gcc client.c -o client

flash: config_io_o_h.hex
	python3 ../util/caravel_hkflash.py config_io_o_h.hex
	python3 ../util/caravel_hkstop.py

flash2: config_io_o_h.hex
	python3 ../util/caravel_flash.py config_io_o_h.hex

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd

.PHONY: clean hex all flash

