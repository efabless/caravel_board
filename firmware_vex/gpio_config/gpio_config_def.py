#!/bin/env python3
#
# gpio_config_def.py ---  Provides definition of hold violations between blocks for MPW-2
#
# Input:   Hold violations between each GPIO and desired
# Output:  Configuration bitstreams for upper and lower gpio chains
#

from bitstring import Bits, BitArray, BitStream
from enum import Enum

# number of IO in the configuration stream for each chain
NUM_IO = 2
# NUM_IO = 10


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
    ['IO[33]', H_INDEPENDENT],
    ['IO[32]', H_INDEPENDENT],
    ['IO[31]', H_NONE],
    ['IO[30]', H_NONE],
    ['IO[29]', H_NONE],
    ['IO[28]', H_NONE],
]

del gpio_h[NUM_IO:]

gpio_l = [
    ['IO[00]', H_NONE],    # <<<< this must be set to NONE
    ['IO[01]', H_NONE],
    ['IO[02]', H_INDEPENDENT],
    ['IO[03]', H_INDEPENDENT],
    ['IO[04]', H_INDEPENDENT],
    ['IO[05]', H_INDEPENDENT],
    ['IO[06]', H_NONE],
    ['IO[07]', H_NONE],
    ['IO[08]', H_NONE],
    ['IO[09]', H_NONE],
]

del gpio_l[NUM_IO:]

# defines these cases of hold violations
# class ConfigType(Enum):
C_MGMT_OUT = 0
C_MGMT_IN = 1
C_USER_BIDIR = 2
C_DISABLE = 3
C_ALL_ONES = 4

config_h = [
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_ALL_ONES,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
]

del config_h[NUM_IO:]

config_l = [
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_DISABLE,
    C_DISABLE,
    C_DISABLE,
]

del config_l[NUM_IO:]

