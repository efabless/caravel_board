from machine import Pin
import time
from flash import flash, erase
from i2c import *
import sys
import pyb


def accurate_delay(delay):
    tm = time.ticks_us()
    tm_add = time.ticks_add(tm, int(delay * 1000))
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

    def reset_fail_count(self, channel):
        self.fail_count[channel] = 0

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

    def send_pulses(self, num_pulses):
        for i in range(0, num_pulses):
            self.set_value(1)
            accurate_delay(25)
            self.set_value(0)
            accurate_delay(25)

    def turn_io_off(self):
        Pin(self.channel).off()


class Test:
    def __init__(
        self, test_name=None, passing_criteria=[], voltage=1.6, sram=1, config_mode=True
    ):
        self.rstb = Dio("MR", True)
        # self.gpio_mgmt_in = Dio("IO_0", False)
        self.gpio_mgmt_in = Dio("IO_37", False)
        if config_mode:
            # self.gpio_mgmt_out = Dio("IO_37", True)
            self.gpio_mgmt_out = Dio("IO_0", True)
        self.test_name = test_name
        self.voltage = voltage
        self.sram = sram
        self.passing_criteria = passing_criteria
        self.supply = ProgSupply()
        self.en_1v8 = Pin("EN_VOUT1", mode=Pin.OUT, value=1)
        self.en_3v3 = Pin("EN_VOUT2", mode=Pin.OUT, value=1)

    def receive_packet(self, num_pulses):
        pulses = 0
        io_pulse = 0
        self.gpio_mgmt_in.set_state(False)
        timeout = time.time() + 10
        state = 0
        num_trans = num_pulses * 2
        while 1:
            val = self.gpio_mgmt_in.get_value()
            if val != state:
                io_pulse = io_pulse + 1
                state = val
            if io_pulse == num_trans:
                pulses = num_pulses
                break
            if time.time() >= timeout:
                return 0
        return pulses

    def send_increment(self):
        self.gpio_mgmt_out.set_state(True)
        self.gpio_mgmt_out.send_pulses(4)

    def send_reset(self):
        self.gpio_mgmt_out.set_state(True)
        self.gpio_mgmt_out.send_pulses(2)

    def apply_reset(self):
        # print("   applying reset on channel 0 device 1")
        self.rstb.set_value(0)

    def release_reset(self):
        # print("   releasing reset on channel 0 device 1")
        self.rstb.set_value(1)

    def flash(self, hex_file):
        # erase() - no longer needed - included in flash
        try:
            flash(f"{hex_file}")
        except:
            print("*** ERROR - attempting to reflash")
            flash(f"{hex_file}", debug=True)

    def apply_gpio_high(self):
        self.gpio_mgmt_out.set_value(1)

    def apply_gpio_low(self):
        self.gpio_mgmt_out.set_value(0)

    def powerup_sequence(self):

        self.en_3v3.off()
        self.en_1v8.off()
        time.sleep(1)

        # Keep 3.3V supply at 3.3V
        self.supply.write_3v3(0x3A)

        # Note:
        # Potentiometer is MCP4661 and has 10k ohms in
        # 257 steps = 38.9 ohms/step.
        # LDO is MIC2211, which has an output equal to
        # R1 = R2 * (Vout / 1.25 - 1)
        # Where R1 is between Vout and Adj and
        # R2 is between Adj and ground.
        # The caravel board has R1 = 360 and
        # R2 = 5k // (500 + potentiometer value)

        R2 = 360 / ((self.voltage / 1.25) - 1)
        Rpot = (1 / (1 / R2 - 1 / 5000)) - 500
        P = Rpot / 38.911
        Pval = int(P)

        # print('Writing ' + str(Pval) + ' to potentiometer.')
        self.supply.write_1v8(Pval)

        time.sleep(1)
        self.en_1v8.on()
        self.en_3v3.on()
        time.sleep(1)

    def change_power(self):

        # Keep 3.3V supply at 3.3V
        self.supply.write_3v3(0x3A)

        R2 = 360 / ((self.voltage / 1.25) - 1)
        Rpot = (1 / (1 / R2 - 1 / 5000)) - 500
        P = Rpot / 38.911
        Pval = int(P)

        self.supply.write_1v8(Pval)

        time.sleep(1)

    def turn_off_devices(self):
        self.en_1v8.off()
        self.en_3v3.off()
        time.sleep(1)

    def turn_off_ios(self):
        for i in range(38):
            Dio(f"IO_{i}").turn_io_off()

    def release_pins(self):
        for i in range(38):
            Dio(f"IO_{i}")


class ProgSupply:
    def __init__(self):
        self.scl = Pin("I2C2_SCL", mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, value=1)
        self.sda = Pin("I2C2_SDA", mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, value=1)
        self.i2c = I2C(scl=self.scl, sda=self.sda)
        self.i2c.init()

    def read_1v8(self):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x0C, start=False, stop=False)
        self.i2c.write_byte(0x51, start=True, stop=False)
        value = self.i2c.read_byte(ack=True, stop=False) << 8
        value |= self.i2c.read_byte(ack=False, stop=True)
        return value

    def write_1v8(self, value):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x10 & value >> 8, start=False, stop=False)
        ack = self.i2c.write_byte(value & 0xFF, start=False, stop=True)
        return ack

    def read_3v3(self):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x1C, start=False, stop=False)
        self.i2c.write_byte(0x51, start=True, stop=False)
        value = self.i2c.read_byte(ack=True, stop=False) << 8
        value |= self.i2c.read_byte(ack=False, stop=True)
        return value

    def write_3v3(self, value):
        self.i2c.write_byte(0x50, start=True, stop=False)
        self.i2c.write_byte(0x10 | (value >> 8), start=False, stop=False)
        ack = self.i2c.write_byte(value & 0xFF, start=False, stop=True)
        return ack


class Led:
    def __init__(self, pin_name):
        self.led = Pin(pin_name, Pin.OUT)

    def blink(self, short=1, long=0):
        delay_short = 300
        delay_long = 600

        self.led.off()
        for i in range(short):
            self.led.on()
            pyb.delay(delay_short)
            self.led.off()
            pyb.delay(delay_short)

        if long > 0:
            pyb.delay(delay_long)

        for i in range(long):
            self.led.on()
            pyb.delay(delay_long)
            self.led.off()
            pyb.delay(delay_long)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def toggle(self):
        if self.led.value():
            self.led.off()
        else:
            self.led.on()
