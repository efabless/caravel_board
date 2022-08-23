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
class HoldType(Enum):
    NONE = 0
    DEPENDENT = 1
    INDEPENDENT = 2

# gpio names and incoming hold violation types

gpio_h = [
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

gpio_l = [
    ['IO[00]', HoldType.NONE],    # <<<< this must be set to NONE
    ['IO[01]', HoldType.NONE],
    ['IO[02]', HoldType.NONE],
    ['IO[03]', HoldType.NONE],
    ['IO[04]', HoldType.NONE],
    ['IO[05]', HoldType.NONE],
    ['IO[06]', HoldType.NONE],
    ['IO[07]', HoldType.NONE],
    ['IO[08]', HoldType.NONE],
    ['IO[09]', HoldType.NONE],
]


# defines these cases of hold violations
class ConfigType(Enum):
    MGMT_OUT = 0
    MGMT_IN = 1
    USER_BIDIR = 2

config_h = [
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
]

config_l = [
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
    ConfigType.MGMT_OUT,
]


