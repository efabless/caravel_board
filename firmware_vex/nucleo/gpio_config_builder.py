#!/bin/env python3
#
# gpio_config_builder.py
#          Build a pair of configuration bit streams for GPIO on MPW-2 accounting for
#          hold violations between gpio blocks.
#
# Input:   Hold violations between each GPIO and desired
# Output:  Configuration bitsteams for upper and lower gpio chains
#

# import gpio and configuration definitions
# from gpio_config_def import NUM_IO, C_MGMT_IN, C_MGMT_OUT, C_USER_BIDIR, C_DISABLE, C_ALL_ONES, \
#                             H_DEPENDENT, H_INDEPENDENT, H_NONE, H_SPECIAL, config_h, config_l, gpio_h, gpio_l, \
#                             C_USER_BIDIR_WPU, C_USER_BIDIR_WPD, C_USER_IN_NP, C_USER_OUT

# from gpio_config_def import *

# number of IO in the configuration stream for each chain
NUM_IO = 19

# defines these cases of hold violations
H_NONE = 0
H_DEPENDENT = 1
H_INDEPENDENT = 2
H_SPECIAL = 3
H_UNKNOWN = 4

# defines these values for IO configurations
C_MGMT_OUT = 0
C_MGMT_IN = 1
C_USER_BIDIR = 2
C_DISABLE = 3
C_ALL_ONES = 4
C_USER_BIDIR_WPU = 5
C_USER_BIDIR_WPD = 6
C_USER_IN_NP = 7
C_USER_OUT = 8

# ------------------------------------------


def setup(arg_gpio_h, arg_gpio_l):
    # parser = argparse.ArgumentParser(description='provide gpio types')
    # parser.add_argument('-gpio_h','-hi', help='provide gpio_h array with H_NONE or H_INDEPENDENT or H_DEPENDENT (None, Independent and dependent)')
    # parser.add_argument('-gpio_l','-l', help='provide gpio_l array with H_NONE or H_INDEPENDENT or H_DEPENDENT (None, Independent and dependent)')
    # parser.add_argument('-num_io','-n', type=int, help='number of ios to work with')
    # parser.add_argument('-config','-c', help='configuration types for now all gpios have the same gpio config C_MGMT_OUT C_MGMT_IN')
    # parser.add_argument('-debug','-d',action='store_true', help='enable debug prints')
    # args = parser.parse_args()
    # if any(v is  None for v in [args.gpio_h, args.gpio_l,args.num_io,args.config]):
    #     print("fatal: you have to provide both -gpio_h and -gpio_l -args.num_io -args.config")
    #     sys.exit()
    # NUM_IO = args.num_io

    # if args.config == "C_MGMT_OUT":
    #     config_l = [C_MGMT_OUT] *19
    #     config_h = [C_MGMT_OUT] *19
    # elif args.config == "C_MGMT_IN":
    #     config_l = [C_MGMT_IN] *19
    #     config_h = [C_MGMT_IN] *19
    # else:
    #     print ("Fatal: incorrect -config value it has to be C_MGMT_OUT or C_MGMT_IN")
    #     sys.exit()

    gpio_h=list()
    gpio_l=list()
    # arg_gpio_h = args.gpio_h
    arg_gpio_h = arg_gpio_h.replace('[','').replace(']','')
    arg_gpio_h = arg_gpio_h.split(',')
    for i,violation in enumerate(arg_gpio_h):
        if violation == 'H_NONE': violation_type = H_NONE
        elif violation == 'H_INDEPENDENT': violation_type = H_INDEPENDENT
        elif violation == 'H_DEPENDENT': violation_type = H_DEPENDENT
        else :
            print (f"incorrect violation type inside provided argument gpio_h {arg_gpio_h} it has to be H_NONE or H_INDEPENDENT or H_DEPENDENT")
        #     sys.exit()
        gpio_h.append([f'IO[{37-i}]',violation_type])
    # del gpio_h[args.num_io:]
    # if (args.debug):
    #     print(f"gpio_h {gpio_h}")
    # arg_gpio_l = args.gpio_l
    arg_gpio_l = arg_gpio_l.replace('[','').replace(']','')
    arg_gpio_l = arg_gpio_l.split(',')
    # python gpio_config_builder.py -gpio_h [H_NONE,H_DEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_DEPENDENT,H_INDEPENDENT,H_DEPENDENT,H_DEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT]  -gpio_l [H_NONE,H_DEPENDENT,H_DEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_DEPENDENT,H_DEPENDENT,H_INDEPENDENT,H_DEPENDENT,H_DEPENDENT,H_INDEPENDENT,H_DEPENDENT,H_DEPENDENT,H_INDEPENDENT,H_DEPENDENT,H_DEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT,H_INDEPENDENT] -n 8
    for i,violation in enumerate(arg_gpio_l):
        if violation == 'H_NONE': violation_type = H_NONE
        elif violation == 'H_INDEPENDENT': violation_type = H_INDEPENDENT
        elif violation == 'H_DEPENDENT': violation_type = H_DEPENDENT
        else :
            print (f"incorrect violation type inside provided argument gpio_l {arg_gpio_l} it has to be H_NONE or H_INDEPENDENT or H_DEPENDENT")
        #     sys.exit()
        gpio_l.append([f'IO[{i}]',violation_type])
    # del gpio_l[args.num_io:]
    # if (args.debug):
    #     print(f"gpio_l {gpio_l}")
    return gpio_h, gpio_l


def build_stream_dependent(stream, config):
    s = ""
    if config == C_MGMT_OUT:
        # stream += '0b1100000001001'
        s = stream + '1100000000001'
    elif config == C_MGMT_IN:
        s = stream + '1000000000011'
    elif config == C_DISABLE:
        s = stream + '0000000000000'
    elif config == C_ALL_ONES:
        s = stream + '1111111111111'
    elif config == C_USER_BIDIR_WPU:
        s = stream + '0100000000000'
    elif config == C_USER_BIDIR_WPD:
        s = stream + '0110000000000'
    elif config == C_USER_IN_NP:
        # s = stream + '0010000000010'
        s = stream + '0010000000011'
    elif config == C_USER_OUT:
        s = stream + '0110000000010'
    else:
        s = stream + '1100000000000'
    return s


def build_stream_independent(stream, config):
    s = ""
    if config == C_MGMT_OUT:
        # stream += '110000000100'
        s = stream + '110000000000'
    elif config == C_MGMT_IN:
        s = stream + '100000000001'
    elif config == C_DISABLE:
        s = stream + '000000000000'
    elif config == C_ALL_ONES:
        s = stream + '111111111111'
    elif config == C_USER_BIDIR_WPU:
        s = stream + '010000000000'
    elif config == C_USER_BIDIR_WPD:
        s = stream + '011000000000'
    elif config == C_USER_IN_NP:
        s = stream + '001000000001'
    elif config == C_USER_OUT:
        s = stream + '00110000000010'
    else:
        s = stream + '110000000000'
    return s


def build_stream_none(stream, config, bypass):
    s = ""
    if config == C_MGMT_OUT:
        # stream += '1100000001001'
        s = stream + '1100000000001'
    elif config == C_MGMT_IN and bypass:
        s = stream + '0010000000011'
    elif config == C_MGMT_IN:
        s = stream + '1000000000011'
    elif config == C_DISABLE:
        s = stream + '0000000001011'
    elif config == C_ALL_ONES:
        s = stream + '1111111111111'
    elif config == C_USER_BIDIR_WPU:
        s = stream + '0100000000000'
    elif config == C_USER_BIDIR_WPD:
        s = stream + '0110000000000'
    elif config == C_USER_IN_NP:
        s = stream + '0010000000010'
    elif config == C_USER_OUT:
        s = stream + '0110000000010'
    else:
        s = stream + '1100000000000'
    return s


def build_stream_special(stream, config):
    s = ""
    s = stream + str(config)
    return s


def correct_dd_holds(stream, bpos):
    skip = False
    bits = list(stream)
    for x in range(1,bpos):
        if bits[x] == '0' and bits[x-1] == '1' and not skip:
            bits[x] = '1'
            skip = True
        else:
            skip = False
    return "".join(bits)

# ------------------------------------------


def build_config(arg_gpio_h, arg_gpio_l, flag, bypass):
    if flag:
        gpio_h, gpio_l = setup(arg_gpio_h, arg_gpio_l)
    else:
        gpio_h = arg_gpio_h
        gpio_l = arg_gpio_l
    clock = 1
    stream_h = ""
    stream_l = ""
    # config_l = [C_MGMT_OUT] * 19
    # config_h = [C_MGMT_IN] + [C_MGMT_OUT] * 18
    config_h = [C_MGMT_OUT] * 19
    config_l = [C_MGMT_IN] + [C_MGMT_OUT] * 18
    config_stream = []

    # iterate through each IO in reverse order (e.g. IO[30] to IO[37])
    for k in reversed(range(NUM_IO)):

        # build upper IO stream
        if gpio_h[k][1] == H_DEPENDENT:
            stream_h = build_stream_dependent(stream_h, config_h[k])
        elif gpio_h[k][1] == H_INDEPENDENT or gpio_h[k][1] == H_UNKNOWN:
            stream_h = build_stream_independent(stream_h, config_h[k])
        elif gpio_h[k][1] == H_SPECIAL:
            stream_h = build_stream_special(stream_h, config_h[k])
        else:
            stream_h = build_stream_none(stream_h, config_h[k], bypass)

        # build lower IO stream
        if gpio_l[k][1] == H_DEPENDENT:
            stream_l = build_stream_dependent(stream_l, config_l[k])
        elif gpio_l[k][1] == H_INDEPENDENT:
            stream_l = build_stream_independent(stream_l, config_l[k])
        elif gpio_l[k][1] == H_SPECIAL:
            stream_l = build_stream_special(stream_l, config_l[k])
        else:
            stream_l = build_stream_none(stream_l, config_l[k], bypass)

    n_bits = max(len(stream_h), len(stream_l))
    while len(stream_h) < n_bits:
        stream_h = '0' + stream_h
    while len(stream_l) < n_bits:
        stream_l = '0' + stream_l

    bpos_h = len(stream_h)
    bpos_l = len(stream_l)
    for k in range(NUM_IO):

        if gpio_h[k][1] == H_DEPENDENT:
            stream_h = correct_dd_holds(stream_h, bpos_h)

        if gpio_l[k][1] == H_DEPENDENT:
            stream_l = correct_dd_holds(stream_l, bpos_l)

        if gpio_h[k][1] == H_INDEPENDENT:
            bpos_h -= 12
        elif gpio_h[k][1] == H_SPECIAL:
            bpos_h -= len(config_h)
        else:
            bpos_h -= 13

        if gpio_l[k][1] == H_INDEPENDENT:
            bpos_l -= 12
        elif gpio_l[k][1] == H_SPECIAL:
            bpos_l -= len(config_l)
        else:
            bpos_l -= 13

    for k in range(n_bits):
        value = (int(stream_l[k]) << 5) + (int(stream_h[k]) << 6)
        config_stream.append(0x06 + value)
        # config_stream.append(0x16 + value)

    #
    #  create output files
    #

    # print("stream_h   = " + stream_h)
    # print("stream_l   = " + stream_l)
    # print("n_bits = {}".format(n_bits))


    # insert value of n_bits at the beginning of config_stream
    # value increased by one to match the length of the array

    config_stream.insert(0, n_bits+1)

    return config_stream

