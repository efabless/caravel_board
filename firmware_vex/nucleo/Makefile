
DEV=/dev/cu.usbmodem34203

# copies scripts to nucleo
copy:
	mpremote connect ${DEV} repl
	mpremote connect ${DEV} cp main.py flash.py i2c.py :

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

