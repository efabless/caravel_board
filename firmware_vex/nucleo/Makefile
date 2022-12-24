
export PATH=$PATH:/bin:/usr/local/bin/:../../venv/bin:/usr/bin/:.

#DEV=/dev/cu.usbmodem3103
DEV=/dev/cu.usbmodem34203
#DEV=/dev/cu.usbmodem34103
#FILES=main.py flash.mpy i2c.py gpio_config_builder.py config_io_o_h.hex config_io_o_l.hex
#FLASH=/media/efabless/PYBFLASH/
FLASH=//Volumes/PYBFLASH/
NUCLEO_CMD=


boot:
	rshell --port ${DEV} cp boot.py /flash

# pip install rshell to use this target
copy: compile
	mpremote connect ${DEV} cp flash.mpy i2c.mpy gpio_config_builder.mpy nucleo_api.mpy gpio_config_def.mpy :
	mpremote connect ${DEV} cp config_io_o.hex :
	mpremote connect ${DEV} cp io_config.mpy :
	mpremote connect ${DEV} cp main.py :
	mpremote connect ${DEV} ls :

#copy: compile
#	rshell --port ${DEV} cp flash.mpy i2c.mpy gpio_config_builder.mpy nucleo_api.mpy gpio_config_def.mpy /flash
#	rshell --port ${DEV} cp config_io_o.hex /flash
#	rshell --port ${DEV} cp io_config.mpy /flash
#	rshell --port ${DEV} cp main.py /flash
#	rshell --port ${DEV} ls /flash

# copies scripts to nucleo
copy2: compile
	cp flash.mpy i2c.mpy gpio_config_builder.mpy nucleo_api.mpy io_config.mpy ${FLASH}
	cp config_io_o.hex ${FLASH}
	cp main.py ${FLASH}
	ls ${FLASH}

copy3:
	cp flash.py i2c.py gpio_config_builder.py nucleo_api.py io_config.py ${FLASH}
	cp config_io_o.hex ${FLASH}
	cp main.py ${FLASH}
	ls ${FLASH}

# cross compile python to micropython bin.

# mpy-cross is specific to the build machine, not the Nucleo.
# the current executable is for a M1 mac.  it needs to be compiled for other build machines

compile:
	mpy-cross flash.py
	mpy-cross io_config.py
	mpy-cross gpio_config_builder.py
	mpy-cross i2c.py
	mpy-cross nucleo_api.py
	mpy-cross boot.py

# runs script from the local filesystem
reset:
	#mpremote connect ${DEV} soft-reset
	mpremote connect ${DEV} exec "import machine; machine.reset()"

# alternate -- mpremote connect ${DEV} exec "import io_config; io_config.run()"
run:
	mpremote connect ${DEV} exec "import machine; machine.reset()"

get_config:
	mpremote connect ${DEV} cp :gpio_config_def.py .

# enter repl on nucleo
repl:
	mpremote connect ${DEV} repl

# flash micropython firmware image.  this firmware image has been rebuilt to add pins for the Caravel Nucleo Hat
F746ZG: compile
	st-flash --connect-under-reset --format ihex write F746ZG_firmware.hex
	sleep 5
	cp flash.mpy i2c.mpy gpio_config_builder.mpy nucleo_api.mpy io_config.mpy ${FLASH}
	cp config_io_o.hex ${FLASH}
	cp main.py ${FLASH}
	ls ${FLASH}

F413ZH:
	st-flash --connect-under-reset --format ihex write F413ZH_firmware.hex
	sleep 7
	cp flash.py i2c.py gpio_config_builder.py nucleo_api.py io_config.py ${FLASH}
	cp config_io_o.hex ${FLASH}
	cp main.py ${FLASH}
	ls ${FLASH}

# ---- targets for building hex file

#TOOLCHAIN_PATH=/foss/tools/riscv-gnu-toolchain-rv32i/217e7f3debe424d61374d31e33a091a630535937/bin/
TOOLCHAIN_PATH=/usr/local/bin/
#TOOLCHAIN_PATH=/opt/riscv32imc/bin/

# Set the prefix for `riscvXX-unknown-elf-*`
# On installations using `multilib`, this will be `riscv64` even for compiling to 32-bit targets
TOOLCHAIN_PREFIX=riscv64-unknown-elf
#TOOLCHAIN_PREFIX=riscv32-unknown-linux-gnu

SED_CMD=sed -i '.orig' -e
#SED_CMD=sed -ie

.SUFFIXES:

PATTERN = config_io_o

hex:  ${PATTERN:=.hex}

%.elf: %.c ../sections.lds ../crt0_vex.S ./gpio_config_data.c ./send_packet.c
	#$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=rv32i -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c ../gpio_program.c $<

	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-gcc -I../ -I../generated/ -O0 -mabi=ilp32 -march=rv32i -D__vexriscv__ -Wl,-Bstatic,-T,../sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ ../crt0_vex.S ../isr.c $<
	${TOOLCHAIN_PATH}$(TOOLCHAIN_PREFIX)-objdump -s  config_io_o.elf > config_io_o.lst

%.hex: %.elf
	#$(TOOLCHAIN_PATH)riscv32-unknown-linux-gnu-objcopy -O verilog $< $@
	$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-objcopy -O verilog $< $@
	$(SED_CMD) 's/@10/@00/g' $@
	$(SED_CMD) '1,/@00/!d' $@

clean:
	rm -f *.elf config_io_o.hex

.PHONY: clean image hex copy repl run
