#!/bin/env python3
#
# gpio_config_builder.py
#          Build a pair of configuration bit streams for GPIO on MPW-2 accounting for
#          hold violations between gpio blocks.
#
# Input:   Hold violations between each GPIO and desired
# Output:  Configuration bitsteams for upper and lower gpio chains
#

from bitstring import Bits, BitArray, BitStream
from enum import Enum

# import gpio and configuration definitions
# from gpio_config_def import NUM_IO, C_MGMT_IN, C_MGMT_OUT, C_USER_BIDIR, C_DISABLE, C_ALL_ONES, \
#                             H_DEPENDENT, H_INDEPENDENT, H_NONE, H_SPECIAL, config_h, config_l, gpio_h, gpio_l, \
#                             C_USER_BIDIR_WPU, C_USER_BIDIR_WPD, C_USER_IN_NP, C_USER_OUT

from gpio_config_def import *

# ------------------------------------------


stream_h = BitStream()
stream_l = BitStream()
config_stream = []


def build_stream_dependent(stream, config):
    if config == C_MGMT_OUT:
        # stream.append('0b1100000001001')
        stream.append('0b1100000000001')
    elif config == C_MGMT_IN:
        stream.append('0b1000000000011')
    elif config == C_DISABLE:
        stream.append('0b0000000000000')
    elif config == C_ALL_ONES:
        stream.append('0b1111111111111')
    elif config == C_USER_BIDIR_WPU:
        stream.append('0b0100000000000')
    elif config == C_USER_BIDIR_WPD:
        stream.append('0b0110000000000')
    elif config == C_USER_IN_NOPULL:
        # stream.append('0b0010000000010')
        stream.append('0b0010000000011')
    elif config == C_USER_OUT:
        stream.append('0b0110000000010')
    else:
        stream.append('0b1100000000000')


def build_stream_independent(stream, config):
    if config == C_MGMT_OUT:
        # stream.append('0b110000000100')
        stream.append('0b110000000000')
    elif config == C_MGMT_IN:
        stream.append('0b100000000001')
    elif config == C_DISABLE:
        stream.append('0b000000000000')
    elif config == C_ALL_ONES:
        stream.append('0b111111111111')
    elif config == C_USER_BIDIR_WPU:
        stream.append('0b010000000000')
    elif config == C_USER_BIDIR_WPD:
        stream.append('0b011000000000')
    elif config == C_USER_IN_NOPULL:
        stream.append('0b001000000001')
    elif config == C_USER_OUT:
        stream.append('0b00110000000010')
    else:
        stream.append('0b110000000000')


def build_stream_none(stream, config):
    if config == C_MGMT_OUT:
        # stream.append('0b1100000001001')
        stream.append('0b1100000000001')
    elif config == C_MGMT_IN:
        stream.append('0b1000000000011')
    elif config == C_DISABLE:
        stream.append('0b0000000001011')
    elif config == C_ALL_ONES:
        stream.append('0b1111111111111')
    elif config == C_USER_BIDIR_WPU:
        stream.append('0b0100000000000')
    elif config == C_USER_BIDIR_WPD:
        stream.append('0b0110000000000')
    elif config == C_USER_IN_NOPULL:
        stream.append('0b0010000000010')
    elif config == C_USER_OUT:
        stream.append('0b0110000000010')
    else:
        stream.append('0b1100000000000')


def build_stream_special(stream, config):
    stream.append(config)


def correct_dd_holds(stream, bpos):
    # for x in reversed(range(1,bpos)):
    skip = False
    for x in range(1,bpos):
        if stream[x] == 0 and stream[x-1] == 1 and not skip:
            stream[x] = 1
            skip = True
        else:
            skip = False


# ------------------------------------------
clock = 1

# iterate through each IO in reverse order (e.g. IO[30] to IO[37])
for k in reversed(range(NUM_IO)):

    # build upper IO stream
    if gpio_h[k][1] == H_DEPENDENT:
        build_stream_dependent(stream_h, config_h[k])
    elif gpio_h[k][1] == H_INDEPENDENT:
        build_stream_independent(stream_h, config_h[k])
    elif gpio_h[k][1] == H_SPECIAL:
        build_stream_special(stream_h, config_h[k])
    else:
        build_stream_none(stream_h, config_h[k])

    # build lower IO stream
    if gpio_l[k][1] == H_DEPENDENT:
        build_stream_dependent(stream_l, config_l[k])
    elif gpio_l[k][1] == H_INDEPENDENT:
        build_stream_independent(stream_l, config_l[k])
    elif gpio_l[k][1] == H_SPECIAL:
        build_stream_special(stream_l, config_l[k])
    else:
        build_stream_none(stream_l, config_l[k])

n_bits = max(len(stream_h), len(stream_l))
if len(stream_h) < n_bits:
    stream_h.prepend(Bits(length=n_bits-len(stream_h)))
if len(stream_l) < n_bits:
    stream_l.prepend(Bits(length=n_bits-len(stream_l)))

bpos_h = len(stream_h)
bpos_l = len(stream_l)
# for k in reversed(range(NUM_IO)):
# iterate from IO 37 to 35
for k in range(NUM_IO):

    if gpio_h[k][1] == H_DEPENDENT:
        correct_dd_holds(stream_h, bpos_h)

    if gpio_l[k][1] == H_DEPENDENT:
        correct_dd_holds(stream_l, bpos_l)

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
    value = (stream_l[k] << 5) + (stream_h[k] << 6)
    config_stream.append(0x06 + value)
    # config_stream.append(0x16 + value)

#
#  create output files
#

print("stream_h   = " + stream_h.bin)
print("stream_l   = " + stream_l.bin)
print("n_bits = {}".format(n_bits))

f = open("gpio_config_data.py", "w")
f.write("from bitstring import Bits, BitArray, BitStream\n")
f.write("from enum import Enum\n")
f.write("\n")
f.write("config_h = BitStream('0b" + stream_h.bin + "')\n")
f.write("config_l = BitStream('0b" + stream_l.bin + "')\n")
f.close()

f = open("gpio_config_data.c", "w")
f.write("\n")

# f.write("int config_h[] = {")
# for x in stream_h.cut(8):
#     f.write("0x" + x.hex + ", ")
# f.write("};\n")
# f.write("int config_l[] = {")
# for x in stream_l.cut(8):
#     f.write("0x" + x.hex + ", ")
# f.write("};\n")

# f.write('char config_h[] = "')
# for k in range(n_bits):
#     f.write('1' if stream_h[k] else '0')
# f.write('";\n')
#
# f.write('char config_l[] = "')
# for k in range(n_bits):
#     f.write('1' if stream_l[k] else '0')
# f.write('";\n')

f.write("char config_stream[] = {")
for x in config_stream:
    f.write("0x{:02x}, ".format(x))
f.write("};\n")

# f.write("int n_bits = " + str(n_bits*2) + ";\n")
f.write("int n_bits = " + str(n_bits) + ";\n")
f.close()

from bitstring import Bits, BitArray, BitStream
from enum import Enum
