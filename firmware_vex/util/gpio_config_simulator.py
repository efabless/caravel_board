#!/bin/env python3
#
# gpio_reg_simulator.py ---  Simulate GPIO configuration based on data independent
# and dependent hold violations for MPW-2
#
# Input:   Hold violations between each GPIO and input pattern for configuration
# Output:  Results after configuration for each clock cycle
#

from bitstring import Bits, BitArray, BitStream
from enum import Enum


def print_header():
    print("   h:", end=" ")
    for x in gpio_h:
        if x[1] == HoldType.INDEPENDENT:
            print("I", end="")
        elif x[1] == HoldType.DEPENDENT:
            print("D", end="")
        else:
            print("_", end="")
        print("___" + x[0] + "___", end=" ")
    print()
    print("   l:", end=" ")
    for x in gpio_l:
        if x[1] == HoldType.INDEPENDENT:
            print("I", end="")
        elif x[1] == HoldType.DEPENDENT:
            print("D", end="")
        else:
            print("_", end="")
        print("___" + x[0] + "___", end=" ")
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
]

gpio_low_reg = [
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

# defines these cases of hold violations
class HoldType(Enum):
    NONE = 0
    DEPENDENT = 1
    INDEPENDENT = 2

# gpio names and incoming hold violation types

# gpio_h = [
#     ['IO[37]', HoldType.NONE],    # <<<< this must be set to NONE
#     ['IO[36]', HoldType.NONE],
#     ['IO[35]', HoldType.NONE],
#     ['IO[34]', HoldType.NONE],
#     ['IO[33]', HoldType.NONE],
#     ['IO[32]', HoldType.NONE],
#     ['IO[31]', HoldType.NONE],
#     ['IO[30]', HoldType.NONE],
#     ['IO[29]', HoldType.NONE],
#     ['IO[28]', HoldType.NONE],
# ]

# gpio_h = [
#     ['IO[37]', HoldType.NONE],    # <<<< this must be set to NONE
#     ['IO[36]', HoldType.INDEPENDENT],
#     ['IO[35]', HoldType.INDEPENDENT],
#     ['IO[34]', HoldType.INDEPENDENT],
#     ['IO[33]', HoldType.INDEPENDENT],
#     ['IO[32]', HoldType.INDEPENDENT],
#     ['IO[31]', HoldType.INDEPENDENT],
#     ['IO[30]', HoldType.INDEPENDENT],
#     ['IO[29]', HoldType.INDEPENDENT],
#     ['IO[28]', HoldType.INDEPENDENT],
# ]

gpio_h = [
    ['IO[37]', HoldType.NONE],    # <<<< this must be set to NONE
    ['IO[36]', HoldType.INDEPENDENT],
    ['IO[35]', HoldType.INDEPENDENT],
    ['IO[34]', HoldType.INDEPENDENT],
    ['IO[33]', HoldType.INDEPENDENT],
    ['IO[32]', HoldType.INDEPENDENT],
    ['IO[31]', HoldType.DEPENDENT],
    ['IO[30]', HoldType.NONE],
    ['IO[29]', HoldType.NONE],
    ['IO[28]', HoldType.NONE],
]

gpio_l = [
    ['IO[00]', HoldType.NONE],    # <<<< this must be set to NONE
    ['IO[01]', HoldType.INDEPENDENT],
    ['IO[02]', HoldType.INDEPENDENT],
    ['IO[03]', HoldType.INDEPENDENT],
    ['IO[04]', HoldType.INDEPENDENT],
    ['IO[05]', HoldType.INDEPENDENT],
    ['IO[06]', HoldType.DEPENDENT],
    ['IO[07]', HoldType.NONE],
    ['IO[08]', HoldType.NONE],
    ['IO[09]', HoldType.NONE],
]

# config_h = [ BitStream('0b1000000000011') ] * 10
# config_h = [ BitStream('0b1111111111110') ] * 10

# config_h = [
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
# ]

# config_h = [
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
#     BitStream('0b1000000000011'),
# ]

config_h = [
    BitStream('0b1000000000011'),  # 37
    BitStream('0b000000000011'),
    BitStream('0b000000000011'),
    BitStream('0b000000000011'),
    BitStream('0b000000000011'),   # 33
    BitStream('0b000000000011'),   # 32
    BitStream('0b1000000000011'),  # 31
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
]

config_l = [
    BitStream('0b1000000000011'),  # 37
    BitStream('0b000000000011'),
    BitStream('0b000000000011'),
    BitStream('0b000000000011'),
    BitStream('0b000000000011'),   # 33
    BitStream('0b000000000011'),   # 32
    BitStream('0b1000000000011'),  # 31
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
]

# ------------------------------------------

print()
print_header()

print("cfgh:", end=" ")
for x in config_h:
    if len(x) < 13:
        print("_"+x.bin, end=" ")
    else:
        print(x.bin, end=" ")
print()
print("cfgl:", end=" ")
for x in config_l:
    if len(x) < 13:
        print("_"+x.bin, end=" ")
    else:
        print(x.bin, end=" ")
print()
print()
print_header()

print("  0h:", end=" ")
for x in gpio_h_reg:
    print(x.bin, end=" ")
print()

clock = 1
# iterate through each IO in reverse order
for k in reversed(range(10)):
# for k in range(10):

    # shift based on the number of bits in the config stream for that register
    # from msb to lsb
    for j in reversed(range(len(config_h[k]))):
        print("{:3d}h:".format(clock), end=" ")
        clock += 1
        saved_bit = last_bit = prev_last_bit = 0

        # iterate through each gpio
        for i in range(len(gpio_h_reg)):

            # store bit to be shifted off    
            saved_bit = gpio_h_reg[i][12]

            # right shift all bits in the register
            gpio_h_reg[i].ror(1)

            if gpio_h[i][1] == HoldType.INDEPENDENT:
                # shift in bit from previous gpio register, skipping the first bit
                gpio_h_reg[i][1] = last_bit
                gpio_h_reg[i][0] = prev_last_bit

            elif gpio_h[i][1] == HoldType.DEPENDENT and prev_last_bit == 0:
                    gpio_h_reg[i][0] = 0

            else:
                # shift in bit from previous gpio register
                gpio_h_reg[i][0] = last_bit

            last_bit = saved_bit
            prev_last_bit = gpio_h_reg[i][12]
        
        # shift in next bit from configuration stream    
        gpio_h_reg[0][0] = config_h[k][j]
        
        for x in gpio_h_reg:
            print(x.bin, end=" ")
        print()

print_header()
