
# copies scripts to nucleo
copy:
	mpremote connect /dev/tty.usbmodem34203 cp main.py :
	mpremote connect /dev/tty.usbmodem34203 soft-reset

# runs script from the local filesystem
run:
	mpremote connect /dev/tty.usbmodem34203 run main.py

# enter repl on nucleo
repl:
	mpremote connect /dev/tty.usbmodem34203 repl

# flash micropython firmware image.  this firmware image has been rebuilt to add pins for the Caravel Nucleo Hat
image:
	st-flash --connect-under-reset --format ihex write firmware.hex

.PHONY: image hex all copy repl run

