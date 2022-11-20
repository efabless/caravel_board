from nucleo_api import *
import os
import gpio_config_builder
from flash import flash_mem
import sys

def run_builder(gpio_l, gpio_h):
    gpio_l = ",".join(gpio_l)
    gpio_h = ",".join(gpio_h)
    return gpio_config_builder.build_config(gpio_h, gpio_l)


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
    print("   Flashing CPU")
    test.apply_reset()
    test.powerup_sequence()
    test.flash(f"{test_name}.hex")
    test.powerup_sequence()
    test.release_reset()


def exec_data_flash(test, test_name, config_stream):
    print("   Flashing CPU")
    test.apply_reset()
    test.powerup_sequence()
    erase()
    test.flash(f"{test_name}.hex")
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
            print(f"start sending pulses to gpio[{channel}]")
            timeout = time.time() + 10
            state = 0
            io_pulse = 0
            while 1:
                val = Dio(f"IO_{channel}").get_value()
                if val != state:
                    io_pulse = io_pulse + 1
                    state = val
                if io_pulse == 8:
                    io_pulse = 0
                    print(f"gpio[{channel}] Passed")
                    break
                if time.time() >= timeout:
                    print(f"Timeout failure on gpio[{channel}]!")
                    return False, channel
        elif pulse_count == 0:
            return False, channel
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
            f = open(f"configuration.py", "a")
            f.write(f"# voltage: {voltage}\n")
            f.write(
                f"# configuration failed in gpio[{channel}], anything after is invalid\n"
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
            f = open(f"configuration.py", "a")
            f.write(f"# voltage: {voltage}\n")
            f.write(
                f"# configuration failed in gpio[{channel}], anything before is invalid\n"
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
        if not high:
            test_result, channel_failed = run_test(test, chain)
        else:
            test_result, channel_failed = run_test(test, chain)
        if test_result:
            print("Test Passed!")
            test_passed(test, gpio_l, gpio_h, chain)
        else:
            gpio_l, gpio_h = change_config(
                channel_failed, gpio_l, gpio_h, test.voltage, test
            )
        if gpio_h.get_gpio_failed() is True or gpio_l.get_gpio_failed() is True:
            break


def test_passed(test, gpio_l, gpio_h, chain):
    f = open(f"configuration.py", "a")
    f.write(f"# voltage: {test.voltage}\n")
    f.write(f"# IO configuration chain was successful\n")
    if chain == "low":
        io = 00
        f.write('gpio_l = [\n')
        for i in gpio_l.array:
            f.write(f'[\'IO[{io}]\', {i}],\n')
            io = io + 1
        f.write(']\n')
    elif chain == "high":
        io = 37
        f.write('gpio_h = [\n')
        for i in gpio_h.array:
            f.write(f'[\'IO[{io}]\', {i}],\n')
            io = io - 1
        f.write(']\n')
    f.close()


def run():
    if "configuration.py" in os.listdir():
        os.remove("configuration.py")
    test = Test()
    gpio_l = Gpio()
    gpio_h = Gpio()

    choose_test(test, "config_io_o", gpio_l, gpio_h)

    gpio_l = Gpio()
    gpio_h = Gpio()
    choose_test(test, "config_io_o", gpio_l, gpio_h, "high", True)
    test.turn_off_devices()
    sys.exit()


if __name__ == "__main__":
    import pyb
    sw = pyb.Switch()
    sw.callback(run())