from nucleo_api import *
import os
import gpio_config_builder
from flash import flash_mem
import sys
from machine import Pin

VERSION = "io_config -- version 1.2.2"
config_filename = "gpio_config_def.py"
debug = False
# debug=True



# used as an activity indicator
#        - active = flash firmware, checking for IO pulses

led_blue = Led("B7")

# used for program start and completion

led_green = Led("B0")

# red and green are used at program termination
#       - flashing red = chain configuration failure

led_red = Led("B14")


def run_builder(gpio_l, gpio_h, bypass):
    """runs the builder to get the configuration stream

    Args:
        gpio_l (class): low chain class
        gpio_h (class): high chain class

    Returns:
        array: configuration stream after running builder
    """

    gpio_l = ",".join(gpio_l)
    gpio_h = ",".join(gpio_h)
    return gpio_config_builder.build_config(gpio_h, gpio_l, True, bypass)


def run_builder_sanity(gpio_l, gpio_h, bypass):
    """runs the builder for the sanity check, where it will skip the initiallization of low and high chain

    Args:
        gpio_l (class): low chain class
        gpio_h (class): high chain class

    Returns:
        array: configuration sream after running builder
    """
    return gpio_config_builder.build_config(gpio_h, gpio_l, False, bypass)


def flash_data(test_name, config_stream, first_line=1):
    """flashes only the data part that changes with the config_stream

    Args:
        test_name (string): name of test
        config_stream (array): description of the bitstream of each IO
        first_line (int, optional): flag to make sure the config_stream is in the correct location. Defaults to 1.
    """
    hex_file = open(f"{test_name}-tmp.hex", "w")
    hex_data = ""
    output_hex = []
    n_bits = config_stream[0]

    with open(f"{test_name}.hex", mode="r") as f:
        line = f.readline()
        line = line.strip()
        while line != "":
            if line.startswith("@"):
                if first_line > 0:
                    first_line = first_line - 1
                else:
                    output_hex = [line.strip()]
                    break
            line = f.readline()

    count = 0
    for d in config_stream:
        hex_data = hex_data + " {:02x}".format(d)
        count = count + 1
        if count >= 16:
            output_hex.append(f"{hex_data[1:]}")
            count = 0
            hex_data = ""

    if hex_data:
        c = 0
        last_line_len = len(hex_data[1:].split())
        if last_line_len <= 8:
            while len(hex_data[1:].split()) < 8:
                hex_data = hex_data + " " + "00"
            hex_data = (
                hex_data
                + " "
                + f"{str(hex(int(n_bits)))[2:].upper()} 00 00 00 00 00 00 00 "
            )
            output_hex.append(f"{hex_data[1:]}")
        elif last_line_len > 8 and last_line_len < 16:
            while len(hex_data[1:].split()) < 16:
                hex_data = hex_data + " " + "00"
            output_hex.append(f"{hex_data[1:]}")
            output_hex.append(
                f"{str(hex(int(n_bits)))[2:].upper()} 00 00 00 00 00 00 00 "
            )
    else:
        output_hex.append(f"{str(hex(int(n_bits)))[2:].upper()} 00 00 00 00 00 00 00 ")
    for i in output_hex:
        hex_file.write(f"{i}\n")
    hex_file.close()

    flash(f"{test_name}-tmp.hex", debug)


def exec_flash_data(test, test_name, config_stream):
    """executes firmware flashing sequence and data flashing

    Args:
        test (class): description of the test about to run
        test_name (string): name of test
        config_stream (string): description of the bitstream of each IO
    """
    print("::::: flashing Caravel :::::")
    test.apply_reset()
    # test.powerup_flash()
    test.powerup_sequence()
    erase()
    # test.flash(f"{test_name}.hex")
    flash(f"{test_name}.hex", debug)
    flash_data(test_name, config_stream)
    test.powerup_sequence()
    test.release_reset()


def run_calibration(test, chain, gpio_l, gpio_h, bypass=False):
    """runs the calibration program

    Args:
        test (class): description of the test about to run
        chain (string): either low or high chain
        gpio_l (class): low chain class
        gpio_h (class): high chain class
        bypass (bool, optional): flag to use bypassing method for analog projects. Defaults to False.

    Returns:
        bool, int: returns passing or failure, if failure returns the channel that failed
    """
    if debug:
        print("    starting test")
    if chain == "low":
        channel = 0
        if bypass:
            last_channel = 13
        else:
            last_channel = 18
        gpio = gpio_l
    else:
        channel = 37
        if bypass:
            last_channel = 12
        else:
            last_channel = 18
        gpio = gpio_h
    for i in range(0, last_channel):
        pulse_count = test.receive_packet(2)
        if debug:
            print(f"    received packet: pulses = {pulse_count}, i = {i}")
        if pulse_count == 2:
            test.apply_gpio_low()
            accurate_delay(500)
            test.send_increment()
            test.apply_gpio_low()
            if chain == "low":
                channel = channel + 1
            else:
                channel = channel - 1
            states = [True, False, True]
            accurate_delay(50)
            count = 0

            for state in states:
                c = 0
                if state:
                    test.apply_gpio_high()
                else:
                    test.apply_gpio_low()
                accurate_delay(50)
                tm = time.ticks_us()
                timeout = time.ticks_add(tm, int(50000))
                while 1:
                    if bypass and channel == 1:
                        if count == 0:
                            print(
                                f"gpio[{channel:02}] - {gpio.get_config(channel):13} >> Skipping"
                            )
                            count = 1
                        break
                    val = Dio(f"IO_{channel}").get_value()
                    if val != state:
                        if chain == "low":
                            print(
                                f"gpio[{channel:02}] - {gpio.get_config(channel):13} >> Failed"
                            )
                        else:
                            print(
                                f"gpio[{channel:02}] - {gpio.get_config(37 - channel):13} >> Failed"
                            )
                        test.apply_gpio_low()
                        led_red.blink(short=2)
                        led_blue.off()
                        return False, channel
                    if time.ticks_us() >= timeout:
                        break
            if bypass and channel == 1:
                count = 0
            elif chain == "low":
                print(f"gpio[{channel:02}] - {gpio.get_config(channel):13} >> Passed")
            else:
                print(
                    f"gpio[{channel:02}] - {gpio.get_config(37 - channel):13} >> Passed"
                )
            led_green.blink()
        elif pulse_count == 0:
            print(f"*** ERROR: failed to receive ready signal from firmware")
            led_red.blink()
            led_blue.off()
            return False, channel

        test.apply_gpio_low()

    led_blue.off()
    return True, None


def change_config(channel, gpio_l, gpio_h, voltage, test, bypass=False):
    """changes default configuration (H_INDEPENDENT) to H_DEPENDENT for failed IO, if it is the second time the failure
    occurs on the IO, it will exit the program

    Args:
        channel (int): channel number
        gpio_l (class): low chain class
        gpio_h (class): high chain class
        voltage (float): voltage of test
        test (class): description of the test about to run
        bypass (bool, optional): flag to use bypassing method for analog projects. Defaults to False.

    Returns:
        class, class: returns gpio_l and gpio_h
    """
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
            f.write("gpio_h = [\n")
            for i in gpio_h.array:
                if io > channel:
                    f.write(f"['IO[{io}]', {i}],\n")
                else:
                    f.write(f"['IO[{io}]', H_UNKNOWN],\n")
                io = io - 1
            f.write("]\n")
            f.close()
            test.turn_off_devices()

    else:
        if (
            bypass
            and channel == 2
            and gpio_l.get_config(1) == "H_INDEPENDENT"
            and gpio_l.get_config(2) == "H_DEPENDENT"
        ):
            print("*** changing IO[01] to H_DEPENDENT, restarting gpio[02]")
            gpio_l.set_config(1, "H_DEPENDENT")
            gpio_l.set_config(2, "H_INDEPENDENT")
            gpio_l.reset_fail_count(2)
        elif gpio_l.get_config(channel) == "H_INDEPENDENT":
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
            f.write("gpio_l = [\n")
            for i in gpio_l.array:
                if io < channel:
                    f.write(f"['IO[{io}]', {i}],\n")
                else:
                    f.write(f"['IO[{io}]', H_UNKNOWN],\n")
                io = io + 1
            f.write("]\n")
            f.close()
            test.turn_off_devices()
    return gpio_l, gpio_h


def choose_test(test, test_name, gpio_l, gpio_h, chain="low", bypass=False):
    """start point of any test, in this case the calibration program

    Args:
        test (class): description of the test about to run
        test_name (string): name of test to run
        gpio_l (class): low chain class
        gpio_h (class): high chain class
        chain (str, optional): either low or high chain. Defaults to "low".
        bypass (bool, optional): flag to use bypassing method for analog projects. Defaults to False.

    Returns:
        bool, int: flag if channel failed, and channel number
    """
    test_result = False
    while not test_result:
        test.test_name = test_name
        config_stream = run_builder(gpio_l.array, gpio_h.array, bypass)
        exec_flash_data(test, test_name, config_stream)
        test_result, channel_failed = run_calibration(
            test, chain, gpio_l, gpio_h, bypass
        )
        if test_result:
            print("**** IO Configuration Test for {} Chain PASSED!!".format(chain))
            test_passed(test, gpio_l, gpio_h, chain)
        else:
            gpio_l, gpio_h = change_config(
                channel_failed, gpio_l, gpio_h, test.voltage, test, bypass=bypass
            )
        if chain == "low" and gpio_l.get_gpio_failed():
            break
        if chain == "high" and gpio_h.get_gpio_failed():
            break

    return test_result, channel_failed


def sanity_check(test, test_name, gpio_l, gpio_h, chain="low"):
    """runs sanity check with an already known def file

    Args:
        test (class): description of the test about to run
        test_name (string): name of test to run
        gpio_l (class): low chain class
        gpio_h (class): high chain class
        chain (str, optional): either low or high chain. Defaults to "low".

    Returns:
        bool, int: flag if channel failed, and channel number
    """
    import gpio_config_def
    bypass = gpio_config_def.analog

    test_result = False
    channel_failed_h = None
    channel_failed_l = None
    while not test_result:
        test.test_name = test_name
        config_stream = run_builder_sanity(
            gpio_config_def.gpio_l, gpio_config_def.gpio_h, bypass
        )
        exec_flash_data(test, test_name, config_stream)
        test_result, channel_failed = run_calibration(
            test, chain, gpio_l, gpio_h, bypass
        )
        for i in gpio_config_def.gpio_h:
            if i[1] == 4:
                channel_failed_h = int(i[0].split("[")[1].split("]")[0])
                break
        for i in gpio_config_def.gpio_l:
            if i[1] == 4:
                channel_failed_l = int(i[0].split("[")[1].split("]")[0])
                break
        if chain == "low" and channel_failed == channel_failed_l:
            print("**** SANITY CHECK FOR LOW CHAIN PASSED!!")
            test_result = True
            break
        elif chain == "low" and channel_failed != channel_failed_l:
            print("**** SANITY CHECK FOR LOW CHAIN FAILED!!")
            break
        elif chain == "high" and channel_failed == channel_failed_h:
            print("**** SANITY CHECK FOR HIGH CHAIN PASSED!!")
            test_result = True
            break
        elif chain == "high" and channel_failed != channel_failed_h:
            print("**** SANITY CHECK FOR HIGH CHAIN FAILED!!")
            break

    return test_result, channel_failed


def test_passed(test, gpio_l, gpio_h, chain):
    """writes out the def file if test passed

    Args:
        test (class): description of the test about to run
        gpio_l (class): low chain class
        gpio_h (class): high chain class
        chain (str, optional): either low or high chain. Defaults to "low".
    """
    f = open(config_filename, "a")
    f.write(f"# voltage: {test.voltage}\n")
    f.write(f"# IO configuration chain was successful\n")
    if chain == "low":
        io = 00
        f.write("gpio_l = [\n")
        for i in gpio_l.array:
            f.write(f"['IO[{io}]', {i}],\n")
            io = io + 1
        f.write("]\n")
    elif chain == "high":
        io = 37
        f.write("gpio_h = [\n")
        for i in gpio_h.array:
            f.write(f"['IO[{io}]', {i}],\n")
            io = io - 1
        f.write("]\n")
    f.close()


def version():
    """prints the version of the program"""
    print(f"{VERSION}")


def run_poweron(v=1.6):
    """powers on the caravel board through the nucleo

    Args:
        v (float, optional): voltage to power on. Defaults to 1.6.
    """
    test = Test(config_mode=False, voltage=v)
    test.apply_reset()
    test.powerup_sequence()
    test.release_reset()


def run_change_power(v):
    """powers on the caravel board through the nucleo

    Args:
        v (float, optional): voltage to power on. Defaults to 1.6.
    """
    test = Test(config_mode=False, voltage=v)
    test.change_power()


def run_flash_caravel(v=1.6):
    """runs flashing sequence on file called firmware.hex

    Args:
        v (float, optional): voltage to power on. Defaults to 1.6.
    """
    test = Test(config_mode=False, voltage=v)
    print("*** flashing Caravel")
    test.apply_reset()
    test.powerup_sequence()
    erase(debug=True)
    if flash(f"firmware.hex", debug=True):
        print("status Good")
    else:
        print("failed!")
    test.powerup_sequence()
    test.release_reset()


def run_sanity_check():
    """Runs the sanity check

    Args:
        voltage (float, optional): voltage used in test. Defaults to 1.6.
        analog (bool, optional): flag to know if the project is analog. Defaults to False.
    """
    import gpio_config_def
    test = Test(voltage=gpio_config_def.voltage)

    gpio_l = Gpio()
    gpio_h = Gpio()

    print(" ")
    print("===================================================================")
    print(f"{VERSION}")
    print(f"voltage = {gpio_config_def.voltage:1.2f}, analog = {gpio_config_def.analog}")
    print("===================================================================")

    print("===================================================================")
    print("== Beginning SANITY for LOW IO chain...                          ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=2)
    low_chain_passed, low_chain_io_failed = sanity_check(
        test, "config_io_o", gpio_l, gpio_h
    )

    gpio_l = Gpio()
    gpio_h = Gpio()

    print(" ")
    print("===================================================================")
    print("== LOW IO chain test complete.  Testing HIGH IO chain...         ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=4)
    high_chain_passed, high_chain_io_failed = sanity_check(
        test, "config_io_o", gpio_l, gpio_h, "high"
    )

    print(" ")
    print("===================================================================")
    print("== HIGH IO chain test complete. SANITY test complete.            ==")
    print("===================================================================")
    print(" ")
    print(" ")
    print("===================================================================")

    if low_chain_passed:
        print("== LOW chain PASSED.                                             ==")
    else:
        print("== LOW chain FAILED.                                             ==")

    if high_chain_passed:
        print("== HIGH chain PASSED.                                            ==")
    else:
        print("== HIGH chain FAILED.                                            ==")

    print("===================================================================")
    print(" ")
    print("              >>> Press <ctl-c> to exit <<<")

    # test.turn_off_ios()
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


def run(part_name="** unspecified **", voltage=1.6, analog=False):
    """runs the calibration program on both high and low chains

    Args:
        part_name (str, optional): part number. Defaults to "** unspecified **".
        voltage (float, optional): voltage to run the test on. Defaults to 1.6.
        analog (bool, optional): flag to know if project is analog. Defaults to False.
    """

    if config_filename in os.listdir():
        os.remove(config_filename)

    with open(config_filename, "w") as f:
        f.write(f"# gpio_config_def.py file for part {part_name}\n")
        f.write(f"# {VERSION}\n")
        f.write(f"voltage = {voltage:1.2f}\n")
        f.write(f"analog = {analog}\n")
        f.write(f"\n")
        f.write(f"H_NONE        = 0  \n")
        f.write(f"H_DEPENDENT   = 1  \n")
        f.write(f"H_INDEPENDENT = 2  \n")
        f.write(f"H_SPECIAL     = 3  \n")
        f.write(f"H_UNKNOWN     = 4  \n")
        f.write(f"\n")
        f.close()

    test = Test(voltage=voltage)
    gpio_l = Gpio()
    gpio_h = Gpio()

    print(" ")
    print("===================================================================")
    print(f"{VERSION}")
    print(f"voltage = {voltage:1.2f}, analog = {analog}")
    print("===================================================================")

    print(" ")
    print("===================================================================")
    print("== Beginning IO configuration test.  Testing LOW IO chain...     ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=2)
    low_chain_passed, low_chain_io_failed = choose_test(
        test, "config_io_o", gpio_l, gpio_h, bypass=analog
    )

    print(" ")
    print("===================================================================")
    print("== LOW IO chain test complete.  Testing HIGH IO chain...         ==")
    print("===================================================================")
    print(" ")
    led_green.blink(short=3, long=4)
    high_chain_passed, high_chain_io_failed = choose_test(
        test, "config_io_o", gpio_l, gpio_h, "high", bypass=analog
    )

    print(" ")
    print("===================================================================")
    print("== HIGH IO chain test complete. IO configuration test complete.  ==")
    print("===================================================================")
    print(" ")
    print(" ")
    print("===================================================================")
    print("===================================================================")

    if low_chain_passed and analog:
        print("== LOW chain PASSED.   Valid IO = 0 thru 13.                      ==")
    elif low_chain_passed:
        print("== LOW chain PASSED.   Valid IO = 0 thru 18.                      ==")
    else:
        print(
            "== LOW chain FAILED.   Valid IO = 0 thru {:02}.                      ==".format(
                low_chain_io_failed - 1
            )
        )

    if high_chain_passed and analog:
        print("== HIGH chain PASSED.  Valid IO = 25 thru 37.                     ==")
    elif high_chain_passed:
        print("== HIGH chain PASSED.  Valid IO = 19 thru 37.                     ==")
    else:
        print(
            "== HIGH chain FAILED.  Valid IO = {:02} thru 37.                    ==".format(
                high_chain_io_failed + 1
            )
        )

    print("===================================================================")
    print(" ")
    print(
        "*** Run 'make get_config' to retrieve IO configure file ({})\n".format(
            config_filename
        )
    )
    print(" ")
    print("              >>> Press <ctl-c> to exit <<<")

    # test.turn_off_ios()
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
