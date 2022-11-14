from machine import Pin, SPI, SoftSPI, sleep, SoftI2C, reset
from pyb import LED, Timer
from time import sleep
from i2c import I2C
from main import choose_test, Gpio

class prog_supply:
    
    def __init__(self):
        self.scl = Pin('I2C2_SCL', mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, value=1)
        self.sda = Pin('I2C2_SDA', mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, value=1)
        self.i2c = I2C(scl=self.scl, sda=self.sda)
        self.i2c.init()
        
    def read_1v8(self):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x0c, start=False, stop=False)
        self.i2c.write_byte(0x51, start=True, stop=False)
        value = self.i2c.read_byte(ack=True, stop=False) << 8
        value |= self.i2c.read_byte(ack=False, stop=True)
        return value
    
    def write_1v8(self, value):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x10 & value >> 8, start=False, stop=False)
        ack = self.i2c.write_byte(value & 0xff, start=False, stop=True)
        return ack

    def read_3v3(self):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x1c, start=False, stop=False)
        self.i2c.write_byte(0x51, start=True, stop=False)
        value = self.i2c.read_byte(ack=True, stop=False) << 8
        value |= self.i2c.read_byte(ack=False, stop=True)
        return value

    def write_3v3(self, value):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x10 | (value >> 8), start=False, stop=False)
        ack = self.i2c.write_byte(value & 0xff, start=False, stop=True)
        return ack


def read_io_all():
    v = 0
    for i in range(38):
        v = v << 1
        v |= io[i].value() & 0x01
    return v


def write_io_all(v):
    for i in range(38):
        io[i].value(v)


io = []


def setup_io():
    for x in range(38):
        # io.append(Pin('IO_'+str(x), mode=Pin.OUT))
        io.append(Pin('IO_' + str(x), mode=Pin.IN, pull=None))

class Test:
    test_name = "junk"

# -----------------------------------


rst = Pin('MR', mode=Pin.OUT, value=1)
en_1v8 = Pin('EN_VOUT1', mode=Pin.OUT, value=1)
en_3v3 = Pin('EN_VOUT2', mode=Pin.OUT, value=1)

# setup user LEDs
#led_green = LED(1)
#led_blue = LED(2)
#led_red = LED(3)

#pb5 = Pin('TIM3_CH2', mode=Pin.OUT)
#tim = Timer(3, freq=10_000_000)
#ch = tim.channel(2, mode=Timer.PWM, pin=pb5)
#ch.pulse_width_percent(50)
    
#tim.init(period=1, callback=timer_callback)
#pb5.on()
#pwm = PWM(pb5)
#pwm.init(freq=1000000, duty_ns=500)

#for x in range(2):
#    sleep(0.3)
#    led_red.toggle()
#    led_green.toggle()
#    led_blue.toggle()

sleep(2)

ps = prog_supply()
#ps.write_1v8(0x1f)  #1.6V
ps.write_1v8(0x11)  #1.7V
#ps.write_1v8(0x0b)  #1.8V
ps.write_3v3(0x3a)
print("1v8 = {}".format(hex(ps.read_1v8())))
print("3v3 = {}".format(hex(ps.read_3v3())))

rst.off()
sleep(1)
en_1v8.off()
en_3v3.off()
sleep(1)
en_3v3.on()
en_1v8.on()
sleep(1)

#check()

reset()
flash("blink.hex")

rst.on()

#setup_io()

#gpio_l = Gpio()
#gpio_h = Gpio()
#start_time = 0
#test = {}
#test = Test()

#choose_test(test, "config_io_o_l", gpio_l, gpio_h, start_time, "junk")

print("\nRunning...")

while False:
    #sleep(0.5)
    #print(".")
    #led_green.toggle()
    # write_io_all(1)
#    _data = "{:038b}".format(read_io_all())
    data = ""
    for x in _data:
        data = x + data
#    print("{} {} {} {} {} {} {} {} {} {}".format(\
#        data[0:4],data[4:8],data[8:12],data[12:16],data[16:20],data[20:24],data[24:28],data[28:32],data[32:36],data[36:38]))
    #sleep(0.5)
    #print(".")
    #led_green.toggle()
    # write_io_all(0)
    #print(bin(read_io_all()))

print("Done.")