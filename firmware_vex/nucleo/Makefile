
#DEV=/dev/cu.usbmodem3103
DEV=/dev/cu.usbmodem34203
#FILES=main.py flash.mpy i2c.py gpio_config_builder.py config_io_o_h.hex config_io_o_l.hex


 boot:
	rshell --port ${DEV} cp boot.py /flash

# pip install rshell to use this target
 copy: compile
	rshell --port ${DEV} repl ~ import machine ~ machine.reset()
	rshell --port ${DEV} cp flash.mpy i2c.py gpio_config_builder.mpy nucleo_api.py gpio_config_def.py /flash
	rshell --port ${DEV} cp config_io_o_h.hex /flash
	rshell --port ${DEV} cp config_io_o_l.hex /flash
	rshell --port ${DEV} cp io_config.mpy /flash
	rshell --port ${DEV} cp main.py /flash
	rshell --port ${DEV} ls /flash

# copies scripts to nucleo
copy2: compile
	cp flash.py i2c.mpy gpio_config_builder.mpy nucleo_api.mpy gpio_config_def.mpy /media/efabless/PYBFLASH/
	cp config_io_o_h.hex /media/efabless/PYBFLASH/
	cp config_io_o_l.hex /media/efabless/PYBFLASH/
	ls /media/efabless/PYBFLASH/

# cross compile python to micropython bin
compile:
	mpy-cross flash.py
	mpy-cross io_config.py
	mpy-cross gpio_config_builder.py
	mpy-cross i2c.py
	mpy-cross nucleo_api.py
	mpy-cross gpio_config_def.py
	mpy-cross boot.py
	mpy-cross test.py

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

