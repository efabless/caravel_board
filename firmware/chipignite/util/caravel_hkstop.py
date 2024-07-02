#!/usr/bin/env python3

# caravel_hkstop.py:  Access the FTDI chip as an asyncronous
# bit-bang GPIO device, and set all the channels to inputs,
# which will tristate the outputs, allowing the housekeeping
# SPI channels to be used by the Caravel chip for output
# (e.g., for the SPI master)
#

from pyftdi.gpio import GpioAsyncController
from caravel.find_ftdi import find_ftdi

gpio = GpioAsyncController()

# Configure:  A zero bit in direction indicates input, so this sets all
# 8 channels on the ADBUS to input.
gpio.configure(find_ftdi(), direction=0x00, frequency=1e3, initial=0x0)
port = gpio.get_gpio()

# port.set_direction(0b110100000000, 0b110100000000)  # (mask, dir)

# Could put stuff here. . .

input()

gpio.close()

