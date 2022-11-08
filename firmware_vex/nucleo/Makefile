
DEV=/dev/cu.usbmodem3103
#DEV=/dev/cu.usbmodem34203

# copies scripts to nucleo
copy:
	mpremote connect ${DEV} soft-reset
	mpremote connect ${DEV} cp bitstring.mpy :
	mpremote connect ${DEV} cp main.py :
	mpremote connect ${DEV} cp flash.mpy :
	mpremote connect ${DEV} cp i2c.py :
	mpremote connect ${DEV} cp io_config.py :
	mpremote connect ${DEV} cp gpio_config_builder.py :
	mpremote connect ${DEV} cp gpio_config_def.py :

copy-hex:
	mpremote connect ${DEV} cp debug_io.hex :
	#mpremote connect ${DEV} cp blink.hex :

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

