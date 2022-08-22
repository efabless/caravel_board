#!/bin/env python3
#
# gpio_config_builder.py ---  Build a pair of configuration bit streams for GPIO on MPW-2 accounting for
#                          hold violations between gpio blocks.
#
# Input:   Hold violations between each GPIO and desired
# Output:  Configuration bitsteams for upper and lower gpio chains
#

from bitstring import Bits, BitArray, BitStream
from enum import Enum

# import gpio and configuration definitions
from gpio_config_def import NUM_IO, ConfigType, HoldType, config_h, config_l, gpio_h, gpio_l


# ------------------------------------------


stream_h = BitStream()
stream_l = BitStream()


def build_stream_dependent(stream, config):
    # PLACEHOLDER - TO BE UPDATED
    if config == ConfigType.MGMT_OUT:
        stream.append('0b1000000000011')
    elif config == ConfigType.MGMT_IN:
        stream.append('0b1100000000001')
    else:
        stream.append('0b0100000000100')


def build_stream_independent(stream, config):
    # PLACEHOLDER - TO BE UPDATED
    if config == ConfigType.MGMT_OUT:
        stream.append('0b000000000011')
    elif config == ConfigType.MGMT_IN:
        stream.append('0b100000000001')
    else:
        stream.append('0b100000000100')


def build_stream_none(stream, config):
    if config == ConfigType.MGMT_OUT:
        stream.append('0b1000000000011')
    elif config == ConfigType.MGMT_IN:
        stream.append('0b1100000000001')
    else:
        stream.append('0b0100000000100')


def correct_dd_holds(stream):
    for x in range(len(stream)-1):
        if stream[x] == 0 and stream[x+1] == 1:
            stream[x] = 1


# ------------------------------------------

dd_holds_h = 0
dd_holds_l = 0
clock = 1

# count the number of data dependent hold violations
for k in range(NUM_IO):
    if gpio_h[k][1] == HoldType.DEPENDENT:
        dd_holds_h += 1
    if gpio_l[k][1] == HoldType.DEPENDENT:
        dd_holds_l += 1

# iterate through each IO in reverse order
for k in reversed(range(NUM_IO)):

    # build upper IO stream
    if gpio_h[k][1] == HoldType.DEPENDENT:
        build_stream_dependent(stream_h, config_h[k])
    elif gpio_h[k][1] == HoldType.INDEPENDENT:
        build_stream_independent(stream_h, config_h[k])
    else:
        build_stream_none(stream_h, config_h[k])

    # build lower IO stream
    if gpio_l[k][1] == HoldType.DEPENDENT:
        build_stream_dependent(stream_l, config_l[k])
    elif gpio_l[k][1] == HoldType.INDEPENDENT:
        build_stream_independent(stream_l, config_l[k])
    else:
        build_stream_none(stream_l, config_l[k])

for k in reversed(range(NUM_IO)):
    if gpio_h[k][1] == HoldType.DEPENDENT:
        correct_dd_holds(stream_h)
    if gpio_l[k][1] == HoldType.DEPENDENT:
        correct_dd_holds(stream_l)

    # correct_dd_holds(stream_l, dd_holds_l)

print("stream_h   = " + stream_h.bin)
print("stream_l   = " + stream_l.bin)
print()
print("dd_holds_h = {}".format(dd_holds_h))
print("dd_holds_l = {}".format(dd_holds_l))

