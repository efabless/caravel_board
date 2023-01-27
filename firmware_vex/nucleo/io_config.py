from nucleo_api import *
import os
import gpio_config_builder
from flash import flash_mem
import sys
import pyb
from machine import Pin


config_filename = "gpio_config_def.py"


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

# used as an activity indicator
#        - active = flash firmware, checking for IO pulses

led_blue = Led("B7")

# used for program start and completion

led_green = Led("B0")

# red and green are used at program termination
#       - flashing red = chain configuration failure

led_red = Led("B14")


def run_builder(gpio_l, gpio_h):
    gpio_l = ",".join(gpio_l)
    gpio_h = ",".join(gpio_h)
    return gpio_config_builder.build_config(gpio_h, gpio_l, True)


def run_builder_sanity(gpio_l, gpio_h):
    return gpio_config_builder.build_config(gpio_h, gpio_l, False)


def data_flash(test_name, hex_data, first_line=1):
    
    new_hex_file = open(f"{test_name}-tmp.hex", "w")
    new_hex_data = ""
    hex_out = []
    n_bits = hex_data[0]
    
    with open(f"{test_name}.hex", mode='r') as f:
        line = f.readline()
        line = line.strip()
        while line != "":
           if line.startswith("@"):
               if first_line > 0:
                   first_line = first_line - 1
               else:
                   hex_out = [ line.strip() ]
                   break
           line = f.readline()
                    
    count = 0
    for d in hex_data:
        new_hex_data = new_hex_data + " {:02x}".format(d)
        count = count + 1
        if count >= 16:
            hex_out.append(f"{new_hex_data[1:]}")
            count = 0
            new_hex_data = ""

    if new_hex_data:
        c = 0
        last_line_len = len(new_hex_data[1:].split())
        if last_line_len <= 8:
            while len(new_hex_data[1:].split()) < 8:
                new_hex_data = new_hex_data + " " + "00"
            new_hex_data = new_hex_data + " " + f"{str(hex(int(n_bits)))[2:].upper()} 00 00 00 00 00 00 00 "
            hex_out.append(f"{new_hex_data[1:]}")
        elif last_line_len > 8 and last_line_len < 16:
            while len(new_hex_data[1:].split()) < 16:
                new_hex_data = new_hex_data + " " + "00"
            hex_out.append(f"{new_hex_data[1:]}")
            hex_out.append(f"{str(hex(int(n_bits)))[2:].upper()} 00 00 00 00 00 00 00 ")
    else:
        hex_out.append(f"{str(hex(int(n_bits)))[2:].upper()} 00 00 00 00 00 00 00 ")
    for i in hex_out:
        new_hex_file.write(f"{i}\n")
    new_hex_file.close()

    flash(f"{test_name}-tmp.hex")


def exec_flash(test, test_name):
    print("*** Flashing Caravel (1)")
    test.apply_reset()
    test.powerup_sequence()
    test.flash(f"{test_name}.hex")
    test.powerup_sequence()
    test.release_reset()


def exec_data_flash(test, test_name, config_stream):
    print("*** flashing Caravel")
    test.apply_reset()
    test.powerup_sequence()
    erase()
    # test.flash(f"{test_name}.hex")
    flash(f"{test_name}.hex")
    data_flash(test_name, config_stream )
    test.powerup_sequence()
    test.release_reset()


def run_test(test, chain):
    phase = 0
    io_pulse = 0
    if chain == "low":
        channel = 0
        end_pulses = 18
    else:
        channel = 38
        end_pulses = 19
    for i in range(0,end_pulses):
        pulse_count = test.receive_packet()
        if pulse_count == 2:
            if chain == "low":
                channel = channel + 1
            else:
                channel = channel - 1
            #print(f"start sending pulses to gpio[{channel}]")
            timeout = time.time() + 10
            state = 0
            io_pulse = 0
            led_blue.on()
            while 1:
                val = Dio(f"IO_{channel}").get_value()
                if val != state:
                    io_pulse = io_pulse + 1
                    state = val
                if io_pulse == 8:
                    io_pulse = 0
                    print(f"gpio[{channel}] >> Passed")
                    led_green.blink()
                    # led_blue.off()
                    break
                if time.time() >= timeout:
                    print(f"gpio[{channel}] >> TIMED OUT")
                    led_red.blink(short=2)
                    led_blue.off()
                    return False, channel
        elif pulse_count == 0:
            led_red.blink()
            led_blue.off()
            return False, channel

    led_blue.off()
    return True, None


def change_config(channel, gpio_l, gpio_h, voltage, test):
    if channel > 18:
        if gpio_h.get_config(37 - channel) == "H_INDEPENDENT":
            gpio_h.set_config(37 - channel, "H_DEPENDENT")
            gpio_h.increment_fail_count(37 - channel)
        elif gpio_h.get_config(37 - channel) == "H_DEPENDENT":
            gpio_h.set_config(37 - channel, "H_INDEPENDENT")
            gpio_h.increment_fail_count(37 - channel)
        if gpio_h.get_fail_count(37 - channel) > 1:
            gpio_h.gpio_failed()
            f = open(config_filename, "a")
            f.write(f"# voltage: {voltage}\n")
            f.write(
                f"# configuration failed in gpio[{channel}], anything before is invalid\n"
            )
            io = 37
            f.write('gpio_h = [\n')
            for i in gpio_h.array:
                if io > channel:
                    f.write(f'[\'IO[{io}]\', {i}],\n')
                else:
                    f.write(f'[\'IO[{io}]\', H_UNKNOWN],\n')
                io = io - 1
            f.write(']\n')
            f.close()
            test.turn_off_devices()

    else:
        if gpio_l.get_config(channel) == "H_INDEPENDENT":
            gpio_l.set_config(channel, "H_DEPENDENT")
            gpio_l.increment_fail_count(channel)
        elif gpio_l.get_config(channel) == "H_DEPENDENT":
            gpio_l.set_config(channel, "H_INDEPENDENT")
            gpio_l.increment_fail_count(channel)
        if gpio_l.get_fail_count(channel) > 1:
            gpio_l.gpio_failed()
            f = open(config_filename, "a")
            f.write(f"# voltage: {voltage}\n")
            f.write(
                f"# configuration failed in gpio[{channel}], anything after is invalid\n"
            )
            io = 00
            f.write('gpio_l = [\n')
            for i in gpio_l.array:
                if io < channel:
                    f.write(f'[\'IO[{io}]\', {i}],\n')
                else:
                    f.write(f'[\'IO[{io}]\', H_UNKNOWN],\n')
                io = io + 1
            f.write(']\n')
            f.close()
            test.turn_off_devices()
    return gpio_l, gpio_h


def choose_test(
    test,
    test_name,
    gpio_l,
    gpio_h,
    chain="low",
    high=False
):
    test_result = False
    #exec_flash(test, test_name)
    while not test_result:
        test.test_name = test_name
        config_stream = run_builder(gpio_l.array, gpio_h.array)
        exec_data_flash(test, test_name, config_stream)
        test_result, channel_failed = run_test(test, chain)
        if test_result:
            print("**** IO Configuration Test for {} Chain PASSED!!".format(chain))
            test_passed(test, gpio_l, gpio_h, chain)
        else:
            gpio_l, gpio_h = change_config(
                channel_failed, gpio_l, gpio_h, test.voltage, test
            )
        if gpio_h.get_gpio_failed() or gpio_l.get_gpio_failed():
            break

    return test_result, channel_failed


def sanity_check(
    test,
    test_name,
    gpio_l,
    gpio_h,
    chain="low",
    high=False,
):
    import gpio_config_def
    test_result = False
    channel_failed_h = None
    channel_failed_l = None
    while not test_result:
        test.test_name = test_name
        config_stream = run_builder_sanity(gpio_config_def.gpio_l, gpio_config_def.gpio_h)
        exec_data_flash(test, test_name, config_stream)
        test_result, channel_failed = run_test(test, chain)
        for i in gpio_config_def.gpio_h:
            if i[1] == 4:
                channel_failed_h = int(i[0].split('[')[1].split(']')[0])
                break
        for i in gpio_config_def.gpio_l:
            if i[1] == 4:
                channel_failed_l = int(i[0].split('[')[1].split(']')[0])
                break
        if chain == "low" and channel_failed == channel_failed_l:
            print("**** SANITY CHECK FOR LOW CHAIN PASSED!!")
            break
        elif chain == "low" and channel_failed != channel_failed_l:
            print("**** SANITY CHECK FOR LOW CHAIN FAILED!!")
            break
        elif chain == "high" and channel_failed == channel_failed_h:
            print("**** SANITY CHECK FOR HIGH CHAIN PASSED!!")
            break
        elif chain == "high" and channel_failed != channel_failed_h:
            print("**** SANITY CHECK FOR HIGH CHAIN FAILED!!")
            break

    return test_result, channel_failed


def test_passed(test, gpio_l, gpio_h, chain):
    f = open(config_filename, "a")
    f.write(f"# voltage: {test.voltage}\n")
    f.write(f"# IO configuration chain was successful\n")
    if chain == "low":
        low_chain_passed = True
        io = 00
        f.write('gpio_l = [\n')
        for i in gpio_l.array:
            f.write(f'[\'IO[{io}]\', {i}],\n')
            io = io + 1
        f.write(']\n')
    elif chain == "high":
        high_chain_passed = True
        io = 37
        f.write('gpio_h = [\n')
        for i in gpio_h.array:
            f.write(f'[\'IO[{io}]\', {i}],\n')
            io = io - 1
        f.write(']\n')
    f.close()


def run_sanity_check():
    test = Test()

    gpio_l = Gpio()
    gpio_h = Gpio()

    print(" ")
    print("===================================================================")
    print("== Beginning SANITY for LOW IO chain...                          ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=2)
    low_chain_passed, low_chain_io_failed = sanity_check(test, "config_io_o", gpio_l, gpio_h)

    gpio_l = Gpio()
    gpio_h = Gpio()

    print(" ")
    print("===================================================================")
    print("== LOW IO chain test complete.  Testing HIGH IO chain...         ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=4)
    high_chain_passed, high_chain_io_failed = sanity_check(test, "config_io_o", gpio_l, gpio_h, "high", True)

    print(" ")
    print("===================================================================")
    print("== HIGH IO chain test complete. SANITY test complete.            ==")
    print("===================================================================")
    print(" ")
    print(" ")
    print("===================================================================")

    if low_chain_passed:
        print("== LOW chain PASSED.   Valid IO = 0 thru 18.                      ==")
    else:
        print("== LOW chain FAILED.   Valid IO = 0 thru {:02}.                      ==".format(low_chain_io_failed-1))

    if high_chain_passed:
        print("== HIGH chain PASSED.  Valid IO = 19 thru 37.                     ==")
    else:
        print("== HIGH chain FAILED.  Valid IO = {:02} thru 37.                    ==".format(high_chain_io_failed+1))

    print("===================================================================")

    test.turn_off_devices()
    led_blue.off()
    while True:
        if low_chain_passed and high_chain_passed:
            led_green.blink(short=2, long=4)
        elif low_chain_passed:
            led_red.blink(short=2)
            led_green.blink(short=0, long=2)
        elif high_chain_passed:
            led_red.blink(short=2)
            led_green.blink(short=0, long=4)
        else:
            led_red.blink(short=2, long=4)


def run():
    if config_filename in os.listdir():
        os.remove(config_filename)

    with open(config_filename, "a") as f:
        f.write(f"H_NONE        = 0  \n")
        f.write(f"H_DEPENDENT   = 1  \n")
        f.write(f"H_INDEPENDENT = 2  \n")
        f.write(f"H_SPECIAL     = 3  \n")
        f.write(f"H_UNKNOWN     = 4  \n")
        f.write(f"\n")
        f.close()

    test = Test()
    gpio_l = Gpio()
    gpio_h = Gpio()

    print(" ")
    print("===================================================================")
    print("== Beginning IO configuration test.  Testing LOW IO chain...     ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=2)
    low_chain_passed, low_chain_io_failed = choose_test(test, "config_io_o", gpio_l, gpio_h)

    gpio_l = Gpio()
    gpio_h = Gpio()

    print(" ")
    print("===================================================================")
    print("== LOW IO chain test complete.  Testing HIGH IO chain...         ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=4)
    high_chain_passed, high_chain_io_failed = choose_test(test, "config_io_o", gpio_l, gpio_h, "high", True)

    print(" ")
    print("===================================================================")
    print("== HIGH IO chain test complete. IO configuration test complete.  ==")
    print("===================================================================")
    print(" ")
    print(" ")
    print("===================================================================")
    print("===================================================================")

    if low_chain_passed:
        print("== LOW chain PASSED.   Valid IO = 0 thru 18.                      ==")
    else:
        print("== LOW chain FAILED.   Valid IO = 0 thru {:02}.                      ==".format(low_chain_io_failed-1))

    if high_chain_passed:
        print("== HIGH chain PASSED.  Valid IO = 19 thru 37.                     ==")
    else:
        print("== HIGH chain FAILED.  Valid IO = {:02} thru 37.                    ==".format(high_chain_io_failed+1))

    print("===================================================================")
    print(" ")
    print("*** Run 'make get_confg' to retrieve IO configure file ({})\n".format(config_filename))
    test.turn_off_devices()
    led_blue.off()
    while True:
        if low_chain_passed and high_chain_passed:
            led_green.blink(short=2, long=4)
        elif low_chain_passed:
            led_red.blink(short=2)
            led_green.blink(short=0, long=2)
        elif high_chain_passed:
            led_red.blink(short=2)
            led_green.blink(short=0, long=4)
        else:
            led_red.blink(short=2, long=4)
