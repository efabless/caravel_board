# Optional erase to clear existing filesystem.
st-flash erase

# Flash .bin
st-flash write firmware.bin 0x08000000
# or, flash .hex
st-flash --format ihex write firmware.hex

sf-flash reset

https://www.youtube.com/watch?v=DMd3XBDgRWs


https://micropython.org/download/NUCLEO_F746ZG/

Install st-link for flashing micropython firmware
 > brew install stlink

 > pip install mpremote
 > pip install mpy-cross

using mpremote
https://docs.micropython.org/en/latest/reference/mpremote.html

programming
https://docs.micropython.org/en/latest/library/machine.html

building firmware
https://github.com/micropython/micropython/blob/master/ports/stm32/README.md

install thonny
install addon --> adafruit-board-kt

./mpy-cross flash.py  # to create .mpy compiled