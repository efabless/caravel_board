# boot.py -- run on boot to configure USB and filesystem
# Put app code in main.py

import machine
import pyb, sys, os
pyb.country('US') # ISO 3166-1 Alpha-2 code, eg US, GB, DE, AU
#pyb.main('main.mpy') # main script to run after this one
# pyb.usb_mode('VCP') # act as a serial
pyb.usb_mode('VCP+MSC') # act as a serial and a storage device
#pyb.usb_mode('VCP+HID') # act as a serial device and a mouse
# pyb.usb_mode('VCP+MSC', msc=(pyb.SDCard(),))

# if pyb.SDCard().present():
#     os.mount(pyb.SDCard(), '/sd')
#     sys.path[1:1] = ['/sd', '/sd/lib']
