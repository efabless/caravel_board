from nucleo_api import *
import os
import gpio_config_builder
from flash import flash_mem


def run_builder(gpio_l, gpio_h):
    gpio_l = ",".join(gpio_l)
    gpio_h = ",".join(gpio_h)
    return gpio_config_builder.build_config(gpio_h, gpio_l)


def data_flash(test_name, hex_data, first_line=1):
    
    new_hex_file = open(f"{test_name}-tmp.hex", "w")
    #hex_data = []
    new_hex_data = ""
    #for aline in c_file:
    #    aline = aline.strip()
    #    if aline:
    #        if aline.startswith("char"):
    #            idx = aline.find("{")
    #            line = aline[idx + 1 : -4]
    #            data = [item.strip() for item in line.split(",")]
    #        if aline.startswith("int"):
    #            indx = aline.find("=")
    #            arr_size = aline[indx + 1 : -1].strip()
    #            if int(arr_size) > 255:
    #                print(" Array size should be less that 255")
    #                exit(1)
    #for i in data:
    #    hex_data.append(i[2:])

    ## DEBUG
    # print("\nhex_data length = ", len(hex_data))
    # print("hex_data[] = ", hex_data)
    
    # hex_out = ["@00001A00"]
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


    ## DEBUG
    # print("\nhex_out length = ", len(hex_out))
    # print("hex_out[] = ")
    # for x in hex_out:
    #     print(x)
    # input("DEBUG - pausing execution...")
    for i in hex_out:
        new_hex_file.write(f"{i}\n")
        
    #new_hex_file.write(f"{str(hex(int(n_bits)))[2:].upper()} 00 00 00 00 00 00 00 ")
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
    rst = 0
    end_pulses = 0
    while end_pulses < 2:
        pulse_count = test.receive_packet(25)
        if phase == 0 and pulse_count == 1:
            print("Start test")
            phase = phase + 1
        elif phase > 0 and pulse_count == 1:
            rst = rst + 1
            end_pulses = end_pulses + 1
        elif pulse_count > 1:
            end_pulses = 0
            if chain == "low":
                channel = (pulse_count - 2) + (9 * rst)
            elif rst == 1 and chain == "high":
                channel = 28 - (pulse_count - 2)
            elif chain == "high":
                channel = 38 - (pulse_count - 2)
            phase = phase + 1
            print(f"start sending pulses to gpio[{channel}]")
            state = "HI"
            timeout = time.time() + 10
            # accurate_delay(15)
            state = 0
            io_pulse = 0
            while 1:
                # accurate_delay(30)
                # x = Dio(f"IO_{channel}").get_value()
                # if state == "LOW":
                #     if x == True:
                #         state = "HI"
                # elif state == "HI":
                #     if x == False:
                #         state = "LOW"
                #         io_pulse = io_pulse + 1
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
    return True, None


def change_config(channel, gpio_l, gpio_h, voltage, start_time, test):
    end_time = (time.time() - start_time) / 60.0
    if channel > 18:
        if gpio_h.get_config(37 - channel) == "H_INDEPENDENT":
            gpio_h.set_config(37 - channel, "H_DEPENDENT")
            gpio_h.increment_fail_count(37 - channel)
        elif gpio_h.get_config(37 - channel) == "H_DEPENDENT":
            gpio_h.set_config(37 - channel, "H_INDEPENDENT")
            gpio_h.increment_fail_count(37 - channel)
        if gpio_h.get_fail_count(37 - channel) > 1:
            gpio_h.gpio_failed()
            print(f"gpio[{channel}] not working")
            print("Final configuration for gpio_l: ", gpio_l.array)
            print("Final configuration for gpio_h: ", gpio_h.array)
            print(
                "Configuring the ios took: ",
                (time.time() - start_time) / 60.0,
                "minutes",
            )
            f = open(f"configuration.txt", "a")
            f.write(f"voltage: {voltage}\n")
            f.write("Final configuration: \n")
            f.write(
                f"configuration failed in gpio[{channel}], anything after is invalid\n"
            )
            f.write(f"gpio from 37 to 19: {gpio_h.array}\n")
            f.write(f"Execution time: {end_time} minutes\n")
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
            print(f"gpio[{channel}] not working")
            print("Final configuration for gpio_l: ", gpio_l.array)
            print("Final configuration for gpio_h: ", gpio_h.array)
            print(
                "Configuring the ios took: ",
                (time.time() - start_time) / 60.0,
                "minutes",
            )
            f = open(f"configuration.txt", "a")
            f.write(f"voltage: {voltage}\n")
            f.write("Final configuration: \n")
            f.write(
                f"configuration failed in gpio[{channel}], anything after is invalid\n"
            )
            f.write(f"gpio from 0 to 18: {gpio_l.array}\n")
            f.write(f"Execution time: {end_time} minutes\n")
            f.close()
            test.turn_off_devices()
    return gpio_l, gpio_h


def choose_test(
    test,
    test_name,
    gpio_l,
    gpio_h,
    start_time,
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
            print("Final configuration for gpio_l: ", gpio_l.array)
            print("Final configuration for gpio_h: ", gpio_h.array)
            test_passed(test, start_time, gpio_l, gpio_h, chain)
        else:
            gpio_l, gpio_h = change_config(
                channel_failed, gpio_l, gpio_h, test.voltage, start_time, test
            )
        if gpio_h.get_gpio_failed() is True or gpio_l.get_gpio_failed() is True:
            break


def test_passed(test, start_time, gpio_l, gpio_h, chain):
    end_time = (time.time() - start_time) / 60.0

    print("Configuring the ios took: ", end_time, "minutes")

    f = open(f"configuration.txt", "a")
    f.write(f"voltage: {test.voltage}\n")
    f.write(f"configuration of {chain} chain was successful\n")
    f.write(f"Final configuration of {chain} chain: \n")
    if chain == "low":
        f.write(f"gpio from 0 to 18: {gpio_l.array}\n")
    elif chain == "high":
        f.write(f"gpio from 37 to 19: {gpio_h.array}\n")
    f.write(f"Execution time: {end_time} minutes\n")
    f.close()


def run():
    try:
        test = Test()
        gpio_l = Gpio()
        gpio_h = Gpio()

        start_time = time.time()
        start_program = time.time()
        global pid
        pid = None

        choose_test(test, "config_io_o_l", gpio_l, gpio_h, start_time)

        gpio_l = Gpio()
        gpio_h = Gpio()
        start_time = time.time()
        choose_test(test, "config_io_o_h", gpio_l, gpio_h, start_time, "high", True)

        end_time = (time.time() - start_program) / 60.0
        f = open(f"configuration.txt", "a")
        f.write(f"\n\nTotal Execution time: {end_time} minutes")
        f.close()
        test.turn_off_devices()
        exit(0)
    
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            test.turn_off_devices()
            exit(0)
        except SystemExit:
            test.turn_off_devices()
            os._exit(0)


if __name__ == "__main__":
    import pyb
    sw = pyb.Switch()
    sw.callback(run())