from machine import Pin
import time
from flash import flash, erase
from i2c import *
# from pyb import Timer

def accurate_delay(delay):
    tm = time.ticks_us()
    tm_add = time.ticks_add(tm, int(delay*1000))
    while time.ticks_diff(tm_add, time.ticks_us()) > 0:
        pass
    return

class Gpio:
    def __init__(self):
        self.array = []
        self.fail_count = []
        self.failed = False
        self.init_array()
        self.init_fail_count()

    def get_fail_count(self, channel):
        return self.fail_count[channel]

    def init_fail_count(self):
        for i in range(0, 19):
            self.fail_count.append(0)

    def increment_fail_count(self, channel):
        self.fail_count[channel] = self.fail_count[channel] + 1

    def init_array(self):
        for i in range(0, 19):
            if i == 0:
                self.array.append("H_NONE")
            else:
                self.array.append("H_INDEPENDENT")

    def gpio_failed(self):
        self.failed = True

    def get_gpio_failed(self):
        return self.failed

    def set_config(self, channel, config):
        self.array[channel] = config

    def get_config(self, channel):
        return self.array[channel]

class Dio:
    def __init__(self, channel, state=False):
        self.channel = channel
        self.pin = None
        self.state = self.set_state(state)

    def get_value(self):
        val = self.pin.value()
        if val:
            return True
        else:
            return False

    def set_state(self, state):
        if state:
            self.pin = Pin(self.channel, Pin.OUT)
        else:
            self.pin = Pin(self.channel, Pin.IN)

    def set_value(self, value):
        if value:            
            self.pin.value(1)
        else:
            self.pin.value(0)

class Test:
    def __init__(
        self, test_name = None, passing_criteria = [], voltage=1.6, sram=1
    ):
        self.rstb = Dio("MR", True)
        self.gpio_mgmt = Dio("IO_0", True)
        self.test_name = test_name
        self.voltage = voltage
        self.sram = sram
        self.passing_criteria = passing_criteria
        self.supply = ProgSupply()
        self.en_1v8 = Pin('EN_VOUT1', mode=Pin.OUT, value=1)
        self.en_3v3 = Pin('EN_VOUT2', mode=Pin.OUT, value=1)

    def receive_packet(self):
        pulses = 0
        io_pulse = 0
        self.gpio_mgmt.set_state(False)
        timeout = time.time() + 10
        state = 0
        while 1:
            val = self.gpio_mgmt.get_value()
            if val != state:
                io_pulse = io_pulse + 1
                state = val
            if io_pulse == 4:
                pulses = 2
                break
            if time.time() >= timeout:
                return 0
        return pulses

    def apply_reset(self):
        #print("   applying reset on channel 0 device 1")
        self.rstb.set_value(0)

    def release_reset(self):
        #print("   releasing reset on channel 0 device 1")
        self.rstb.set_value(1)

    def flash(self, hex_file):
        # erase() - no longer needed - included in flash
        try:
            flash(f"{hex_file}")
        except:
            print("*** ERROR - attempting to reflash")
            flash(f"{hex_file}", debug=True)

    def powerup_sequence(self):
        self.supply.write_3v3(0x3a)
        if self.voltage == 1.7:
            self.supply.write_1v8(0x11)
        if self.voltage == 1.8:
            self.supply.write_1v8(0x0b)
        if self.voltage == 1.6:
            self.supply.write_1v8(0x1f)
        time.sleep(1)
        self.en_1v8.off()
        self.en_3v3.off()
        time.sleep(1)
        self.en_3v3.on()
        self.en_1v8.on()
        time.sleep(1)

    def turn_off_devices(self):
        self.en_1v8.off()
        self.en_3v3.off()


class ProgSupply:
    
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