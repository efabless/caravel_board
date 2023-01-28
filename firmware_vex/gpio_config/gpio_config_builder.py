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

import os,sys
sys.path.append(os.getcwd())

from gpio_config_def import *
from gpio_config_io import *

# ------------------------------------------


stream_h = ""
stream_l = ""
config_stream = []


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
    elif config == C_USER_IN_NOPULL:
        # s = stream + '0010000000010'
        s = stream + '0010000000011'
    elif config == C_USER_OUT:
        # s = stream + '0110000000010'
        # s = stream + '0110000000010'
        s = stream + '0110000000000'
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
    elif config == C_USER_IN_NOPULL:
        s = stream + '001000000001'
    elif config == C_USER_OUT:
        # s = stream + '00110000000010'
        # s = stream + '011000000001'
        s = stream + '011000000000'
    else:
        s = stream + '110000000000'
    return s


def build_stream_none(stream, config):
    s = ""
    if config == C_MGMT_OUT:
        # stream += '1100000001001'
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
    elif config == C_USER_IN_NOPULL:
        s = stream + '0010000000010'
    elif config == C_USER_OUT:
        # s = stream + '0110000000010'
        s = stream + '0110000000000'
        # s = stream + '0110000000010'
    else:
        s = stream + '1100000000000'
    return s


def build_stream_special(stream, config):
    s = ""
    s = stream + str(config)
    return s


def correct_dd_holds(stream, bpos):
    # for x in reversed(range(1,bpos)):
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
clock = 1

# iterate through each IO in reverse order (e.g. IO[30] to IO[37])
for k in reversed(range(NUM_IO)):

    # build upper IO stream
    if gpio_h[k][1] == H_DEPENDENT:
        stream_h = build_stream_dependent(stream_h, config_h[k])
    elif gpio_h[k][1] == H_INDEPENDENT:
        stream_h = build_stream_independent(stream_h, config_h[k])
    elif gpio_h[k][1] == H_SPECIAL:
        stream_h = build_stream_special(stream_h, config_h[k])
    else:
        stream_h = build_stream_none(stream_h, config_h[k])

    # build lower IO stream
    if gpio_l[k][1] == H_DEPENDENT:
        stream_l = build_stream_dependent(stream_l, config_l[k])
    elif gpio_l[k][1] == H_INDEPENDENT:
        stream_l = build_stream_independent(stream_l, config_l[k])
    elif gpio_l[k][1] == H_SPECIAL:
        stream_l = build_stream_special(stream_l, config_l[k])
    else:
        stream_l = build_stream_none(stream_l, config_l[k])

n_bits = max(len(stream_h), len(stream_l))
while len(stream_h) < n_bits:
    stream_h = '0' + stream_h
while len(stream_l) < n_bits:
    stream_l = '0' + stream_l

bpos_h = len(stream_h)
bpos_l = len(stream_l)
# for k in reversed(range(NUM_IO)):
# iterate from IO 37 to 35
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

config_stream += [0x0] * (247 - len(config_stream))
n_bits = len(config_stream)

#
#  create output files
#

print("stream_h   = " + stream_h)
print("stream_l   = " + stream_l)
print("n_bits = {}".format(n_bits))

f = open("gpio_config_data.py", "w")
# f.write("from bitstring import Bits, BitArray, BitStream\n")
f.write("from enum import Enum\n")
f.write("\n")
f.write("config_data_h = '" + stream_h + "'\n")
f.write("config_data_l = '" + stream_l + "'\n")
f.close()

f = open("gpio_config_data.c", "w")
f.write("\n")

# f.write("int n_bits = " + str(n_bits) + ";\n")

f.write("char config_stream[] = { ")
f.write("0x{:02x}".format(n_bits))
for x in config_stream:
    f.write(", 0x{:02x}".format(x))
f.write(" };\n")

f.close()

