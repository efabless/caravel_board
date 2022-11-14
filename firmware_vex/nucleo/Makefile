
#DEV=/dev/cu.usbmodem3103
DEV=/dev/cu.usbmodem34203
#FILES=main.py flash.mpy i2c.py gpio_config_builder.py config_io_o_h.hex config_io_o_l.hex
FLASH=/media/efabless/PYBFLASH/
#FLASH=//Volumes/PYBFLASH/
#export PATH=$PATH:/bin:/usr/local/bin/:./venv/bin:.

boot:
	rshell --port ${DEV} cp boot.py /flash

# pip install rshell to use this target
copy: compile
	#rshell --port ${DEV} repl ~ import machine ~ machine.reset()
	rshell --port ${DEV} cp flash.mpy i2c.mpy gpio_config_builder.mpy nucleo_api.mpy gpio_config_def.mpy /flash
	rshell --port ${DEV} cp config_io_o_h.hex /flash
	rshell --port ${DEV} cp config_io_o_l.hex /flash
	rshell --port ${DEV} cp io_config.mpy /flash
	rshell --port ${DEV} cp main.py /flash
	rshell --port ${DEV} ls /flash

# copies scripts to nucleo
copy2: compile
	cp flash.mpy i2c.mpy gpio_config_builder.mpy nucleo_api.mpy io_config.mpy ${FLASH}
	cp config_io_o_h.hex ${FLASH}
	cp config_io_o_l.hex ${FLASH}
	cp main.py ${FLASH}
	ls ${FLASH}

# cross compile python to micropython bin
compile:
	mpy-cross flash.py
	mpy-cross io_config.py
	mpy-cross gpio_config_builder.py
	mpy-cross i2c.py
	mpy-cross nucleo_api.py
	mpy-cross boot.py

# runs script from the local filesystem
run:
	mpremote connect ${DEV} soft-reset
	mpremote connect ${DEV} run main.py

# enter repl on nucleo
repl:
	mpremote connect ${DEV} repl

# flash micropython firmware image.  this firmware image has been rebuilt to add pins for the Caravel Nucleo Hat
image:
	st-flash --connect-under-reset --format ihex write nucleo_firmware.hex

.PHONY: image hex all copy repl run
