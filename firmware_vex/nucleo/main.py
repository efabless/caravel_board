from machine import Pin, SPI, SoftSPI, sleep, I2C, SoftI2C
from pyb import LED, Switch
from time import sleep
from flash import flash, check

rst = Pin('MR', mode=Pin.OUT, value=1)


def reset():
    led_blue.on()
    rst.off()
    sleep(0.5)
    rst.on()
    led_blue.off()

sw = Switch()
sw.callback(reset)

# setup user LEDs
led_green = LED(1)
led_blue = LED(2)
led_red = LED(3)

# example IO
io_37 = Pin('IO_37', mode=Pin.OUT, value=0)
io_37.on()
sleep(0.5)
io_37.off()

for x in range(2):
    sleep(0.3)
    led_red.toggle()
    led_green.toggle()
    led_blue.toggle()

sleep(0.5)

# create soft I2C controller
#i2c = I2C('X'', freq=100000)
i2c = SoftI2C(scl='I2C2_SCL', sda='I2C2_SDA', freq=100000)
# i2c.writeto(0x0, bytearray([0xff]))  # 1.8V adjust

cs = Pin('SPI4_CS', mode=Pin.OUT, value=1)
sck = Pin('SPI4_SCK', mode=Pin.OUT, value=0)
mosi = Pin('SPI4_MOSI', mode=Pin.OUT)
miso = Pin('SPI4_MISO', mode=Pin.IN)

# # create soft SPI controller
# spi = SoftSPI(baudrate=400000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
#
# txdata = bytearray([0x40,0x01,0x00,0x00])
# rxdata = bytearray(len(txdata))
#
# cs.value(0)
# spi.write_readinto(txdata, rxdata)
# cs.value(1)
# print(hex(rxdata[2]), hex(rxdata[3]))

flash("blink.hex")

led_red.off()
led_blue.off()

while True:
    sleep(0.5)
    led_green.toggle()
