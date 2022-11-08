
DEV=/dev/cu.usbmodem3103
#DEV=/dev/cu.usbmodem34203
#FILES=main.py flash.mpy i2c.py gpio_config_builder.py bitstring.mpy config_io_o_h.hex config_io_o_l.hex
FILES=main.py flash.mpy i2c.py gpio_config_builder.py bitstring.mpy

# copies scripts to nucleo
copy:
	cp flash.mpy i2c.py gpio_config_builder.py build_hex.py //Volumes/PYBFLASH/
	cp config_io_o_h_1.hex //Volumes/PYBFLASH/
	cp config_io_o_h_2.hex //Volumes/PYBFLASH/
	cp config_io_o_l_1.hex //Volumes/PYBFLASH/
	cp config_io_o_l_2.hex //Volumes/PYBFLASH/
	#cp config_io_o_h.hex //Volumes/PYBFLASH/
	#cp config_io_o_l.hex //Volumes/PYBFLASH/
	#cp bitstring.mpy //Volumes/PYBFLASH/
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

