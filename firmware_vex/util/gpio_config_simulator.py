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

# config_stream = [ BitStream('0b1000000000011') ] * 10

config_stream = [
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
    BitStream('0b1000000000011'),
]

# defines these cases of hold violations
class HoldType(Enum):
    NONE = 0
    DEPENDENT = 1
    INDEPENDENT = 2

# gpio names and incoming hold violation types
gpio = [
    ['IO[37]', HoldType.NONE],    # <<<< this must be set to NONE
    ['IO[36]', HoldType.NONE],
    ['IO[35]', HoldType.NONE],
    ['IO[34]', HoldType.NONE],
    ['IO[33]', HoldType.NONE],
    ['IO[32]', HoldType.NONE],
    ['IO[31]', HoldType.NONE],
    ['IO[30]', HoldType.NONE],
    ['IO[29]', HoldType.NONE],
    ['IO[28]', HoldType.NONE],
]

# gpio shift registers
gpio_reg = [
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

print()
print("   :", end=" ")
for x in gpio:
    if x[1] == HoldType.INDEPENDENT:
        print("I", end="")
    elif x[1] == HoldType.DEPENDENT:
        print("D", end="")
    else:
        print("_", end="")
    print("___" + x[0] + "___", end=" ")

print()

print("  0:", end=" ")
for x in gpio_reg:
    print(x.bin, end=" ")

print()

clock = 1
for k in range(10):
    for j in reversed(range(13)):
        print("{:3d}:".format(clock), end=" ")
        clock += 1
        saved_bit = last_bit = prev_last_bit = 0

        # iterate through each gpio
        for i in range(len(gpio_reg)):

            # store bit to be shifted off    
            saved_bit = gpio_reg[i][12]

            # right shift all bits in the register
            gpio_reg[i].ror(1)

            if gpio[i][1] == HoldType.INDEPENDENT:
                # shift in bit from previous gpio register, skipping the first bit
                gpio_reg[i][1] = last_bit
                gpio_reg[i][0] = prev_last_bit
            if gpio[i][1] == HoldType.DEPENDENT and prev_last_bit == 0:
                    gpio_reg[i][0] = 0
            else:
                # shift in bit from previous gpio register
                gpio_reg[i][0] = last_bit

            last_bit = saved_bit
            prev_last_bit = gpio_reg[i][12]
        
        # shift in next bit from configuration stream    
        gpio_reg[0][0] = config_stream[i][j]
        
        for x in gpio_reg:
            print(x.bin, end=" ")
        print()


