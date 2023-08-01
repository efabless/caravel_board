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
NUM_IO = 19

# defines these cases of hold violations
H_NONE = 0
H_DEPENDENT = 1
H_INDEPENDENT = 2
H_SPECIAL = 3

# gpio names and incoming hold violation types

gpio_h = [
    ['IO[37]', H_NONE],    # <<<< this must be set to NONE
    ['IO[36]', H_DEPENDENT],  # IO[36]
    ['IO[35]', H_INDEPENDENT],  # IO[35]
    ['IO[34]', H_INDEPENDENT],  # IO[34]
    ['IO[33]', H_DEPENDENT],  # IO[33]
    ['IO[32]', H_INDEPENDENT],  # IO[32]
    ['IO[31]', H_INDEPENDENT],  # IO[31]
    ['IO[30]', H_DEPENDENT],  # IO[30]
    ['IO[29]', H_INDEPENDENT],  # IO[29]
    ['IO[28]', H_INDEPENDENT],  # IO[28]
    ['IO[27]', H_INDEPENDENT],  # IO[27]
    ['IO[26]', H_INDEPENDENT],  # IO[26]
    ['IO[25]', H_DEPENDENT],  # IO[25]
    ['IO[24]', H_INDEPENDENT],  # IO[24]
    ['IO[23]', H_INDEPENDENT],  # IO[23]
    ['IO[22]', H_INDEPENDENT],  # IO[22]
    ['IO[21]', H_INDEPENDENT],  # IO[21]
    ['IO[20]', H_INDEPENDENT],  # IO[20]
    ['IO[19]', H_INDEPENDENT],  # IO[19]
]

del gpio_h[NUM_IO:]

gpio_l = [
    ['IO[00]', H_NONE],    # <<<< this must be set to NONE
    ['IO[01]', H_DEPENDENT],  # IO[01]
    ['IO[02]', H_INDEPENDENT],  # IO[02]
    ['IO[03]', H_DEPENDENT],  # IO[03]
    ['IO[04]', H_DEPENDENT],  # IO[04]
    ['IO[05]', H_INDEPENDENT],  # IO[05]
    ['IO[06]', H_INDEPENDENT],  # IO[06]
    ['IO[07]', H_INDEPENDENT],  # IO[07]
    ['IO[08]', H_DEPENDENT],  # IO[08]
    ['IO[09]', H_INDEPENDENT],  # IO[09]
    ['IO[10]', H_INDEPENDENT],  # IO[10]
    ['IO[11]', H_INDEPENDENT],  # IO[11]
    ['IO[12]', H_INDEPENDENT],  # IO[12]
    ['IO[13]', H_DEPENDENT],  # IO[13]
    ['IO[14]', H_INDEPENDENT],  # IO[14]
    ['IO[15]', H_INDEPENDENT],  # IO[15]
    ['IO[16]', H_INDEPENDENT],  # IO[16]
    ['IO[17]', H_INDEPENDENT],  # IO[17]
    ['IO[18]', H_INDEPENDENT],  # IO[18]
]

del gpio_l[NUM_IO:]

# defines these values for IO configurations
C_MGMT_OUT = 0
C_MGMT_IN = 1
C_USER_BIDIR = 2
C_DISABLE = 3
C_ALL_ONES = 4

config_h = [
    C_MGMT_OUT,  #37
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,  #30
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,  #27
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
]

del config_h[NUM_IO:]

config_l = [
    C_DISABLE,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
    C_MGMT_OUT,
]

del config_l[NUM_IO:]

