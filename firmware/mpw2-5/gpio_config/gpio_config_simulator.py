#!/bin/env python3
#
# gpio_reg_simulator.py ---  Simulate GPIO configuration based on data independent
# and dependent hold violations for MPW-2
#
# Input:   Hold violations between each GPIO and input pattern for configuration
# Output:  Results after configuration for each clock cycle
#

import os,sys
sys.path.append(os.getcwd())

from bitstring import Bits, BitArray, BitStream
from enum import Enum
from gpio_config_data import config_data_h, config_data_l
from gpio_config_def import H_NONE, H_DEPENDENT, H_INDEPENDENT, H_SPECIAL, gpio_h, gpio_l

NUM_IO = 19


def print_header(gpio):
    print("    :", end=" ")
    for z in gpio:
        if z[1] == H_INDEPENDENT:
            print("I", end="")
        elif z[1] == H_DEPENDENT:
            print("D", end="")
        elif z[1] == H_SPECIAL:
            print("S", end="")
        else:
            print("_", end="")
        print("___" + z[0] + "___", end=" ")
    print()


# gpio shift registers
gpio_h_reg = [
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
]

del gpio_h_reg[NUM_IO:]

gpio_l_reg = [
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
    BitArray(length=13),
]

del gpio_l_reg[NUM_IO:]

# ------------------------------------------

print_header(gpio_h)

print("   0:", end=" ")
for x in gpio_h_reg:
    print(x.bin, end=" ")
print()

clock = 1
n_clocks = len(config_data_h)
# iterate through each IO in reverse order
# for k in reversed(range(10)):
# for k in reversed(range(len(config_data_h))):
for k in range(len(config_data_h)):
# for k in range(10):

    # shift based on the number of bits in the config stream for that register
    # from msb to lsb
    # for j in reversed(range(len(config_data_h[k]))):
    # while clock <= n_clocks:
    print(" {:3d}:".format(clock), end=" ")
    clock += 1
    current_shifted_out = previous_shifted_out = previous_reg_last_bit = 0

    # iterate through each gpio
    for i in range(len(gpio_h_reg)):

        # store bit to be shifted off
        current_shifted_out = gpio_h_reg[i][12]

        # right shift all bits in the register
        gpio_h_reg[i].ror(1)

        if gpio_h[i][1] == H_INDEPENDENT:
            # shift in bit from previous gpio register, skipping the first bit
            gpio_h_reg[i][1] = previous_shifted_out
            gpio_h_reg[i][0] = previous_reg_last_bit

        elif gpio_h[i][1] == H_DEPENDENT and previous_reg_last_bit == 0:
                gpio_h_reg[i][0] = 0

        else:
            # shift in bit from previous gpio register
            gpio_h_reg[i][0] = previous_shifted_out

        previous_shifted_out = current_shifted_out
        previous_reg_last_bit = gpio_h_reg[i][12]


    # shift in next bit from configuration stream
    # gpio_h_reg[0][0] = config_data_h[k][j]
    gpio_h_reg[0][0] = int(config_data_h[k])

    for x in gpio_h_reg:
        print(x.bin, end=" ")
    print()

print_header(gpio_h)

print()

# ------------------------------------------

print_header(gpio_l)

print("   0:", end=" ")
for x in gpio_l_reg:
    print(x.bin, end=" ")
print()

clock = 1
n_clocks = len(config_data_l)
# iterate through each IO in reverse order
# for k in reversed(range(10)):
# for k in reversed(range(len(config_data_h))):
for k in range(len(config_data_l)):
# for k in range(10):

    # shift based on the number of bits in the config stream for that register
    # from msb to lsb
    # for j in reversed(range(len(config_data_h[k]))):
    # while clock <= n_clocks:
    print(" {:3d}:".format(clock), end=" ")
    clock += 1
    current_shifted_out = previous_shifted_out = previous_reg_last_bit = 0

    # iterate through each gpio
    for i in range(len(gpio_l_reg)):

        # store bit to be shifted off
        current_shifted_out = gpio_l_reg[i][12]

        # right shift all bits in the register
        gpio_l_reg[i].ror(1)

        if gpio_l[i][1] == H_INDEPENDENT:
            # shift in bit from previous gpio register, skipping the first bit
            gpio_l_reg[i][1] = previous_shifted_out
            gpio_l_reg[i][0] = previous_reg_last_bit

        elif gpio_l[i][1] == H_DEPENDENT and previous_reg_last_bit == 0:
                gpio_l_reg[i][0] = 0

        else:
            # shift in bit from previous gpio register
            gpio_l_reg[i][0] = previous_shifted_out

        previous_shifted_out = current_shifted_out
        previous_reg_last_bit = gpio_l_reg[i][12]


    # shift in next bit from configuration stream
    # gpio_h_reg[0][0] = config_data_h[k][j]
    gpio_l_reg[0][0] = int(config_data_l[k])

    for x in gpio_l_reg:
        print(x.bin, end=" ")
    print()

print_header(gpio_l)