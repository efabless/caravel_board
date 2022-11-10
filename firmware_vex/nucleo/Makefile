
#DEV=/dev/cu.usbmodem3103
DEV=/dev/cu.usbmodem34203
#FILES=main.py flash.mpy i2c.py gpio_config_builder.py config_io_o_h.hex config_io_o_l.hex


 boot:
	rshell --port ${DEV} cp boot.py /flash

 copy:
	rshell --port ${DEV} repl ~ import machine ~ machine.reset()
	rshell --port ${DEV} cp flash.mpy i2c.py gpio_config_builder.py /flash
	rshell --port ${DEV} cp config_io_o_h.hex /flash
	rshell --port ${DEV} cp config_io_o_l.hex /flash
	rshell --port ${DEV} cp main.py /flash
	rshell --port ${DEV} ls /flash

# copies scripts to nucleo
copy2:
	cp flash.mpy i2c.py gpio_config_builder.py //Volumes/PYBFLASH/
	cp config_io_o_h.hex //Volumes/PYBFLASH/
	cp config_io_o_l.hex //Volumes/PYBFLASH/
	cp main.py //Volumes/PYBFLASH/
	ls //Volumes/PYBFLASH/

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

