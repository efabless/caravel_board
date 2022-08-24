#!/bin/env python3
#
# gpio_config_def.py ---  Provides definition of hold violations between blocks for MPW-2
#
# Input:   Hold violations between each GPIO and desired
# Output:  Configuration bitsteams for upper and lower gpio chains
#

from bitstring import Bits, BitArray, BitStream
from enum import Enum

# number of IO in the configuration stream for each chain
NUM_IO = 10


# defines these cases of hold violations
# class HoldType(Enum):
H_NONE = 0
H_DEPENDENT = 1
H_INDEPENDENT = 2

# gpio names and incoming hold violation types


gpio_h = [
    ['IO[37]', H_NONE],    # <<<< this must be set to NONE
    ['IO[36]', H_INDEPENDENT],
    ['IO[35]', H_INDEPENDENT],
    ['IO[34]', H_INDEPENDENT],
    ['IO[33]', H_NONE],
    ['IO[32]', H_NONE],
    ['IO[31]', H_NONE],
    ['IO[30]', H_NONE],
    ['IO[29]', H_NONE],
    ['IO[28]', H_NONE],
]

gpio_l = [
    ['IO[00]', H_NONE],    # <<<< this must be set to NONE
    ['IO[01]', H_NONE],
    ['IO[02]', H_NONE],
    ['IO[03]', H_NONE],
    ['IO[04]', H_NONE],
    ['IO[05]', H_NONE],
    ['IO[06]', H_NONE],
    ['IO[07]', H_NONE],
    ['IO[08]', H_NONE],
    ['IO[09]', H_NONE],
]


# defines these cases of hold violations
# class ConfigType(Enum):
C_MGMT_OUT = 0
C_MGMT_IN = 1
C_USER_BIDIR = 2
C_DISABLE = 2

config_h = [
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
]

config_l = [
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
]


