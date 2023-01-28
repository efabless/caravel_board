#!/usr/bin/env python3
#
# gpio_convert.py---
#
#	Convert the bitstreams in gpio_config_data.py into a
#	set of GPIO configuration values for using with an
#	automatic transfer.
#
from gpio_config_data import config_data_h
from gpio_config_data import config_data_l

# Get the length of the bit streams
hlen = len(config_data_h)
llen = len(config_data_l)

# Figure out how much shorter these are than the total
# number of configuration bits
hdiff = (13 * 19) - hlen
ldiff = (13 * 19) - llen

# Pad each binary vector with zeros to make up the total
# bit length of the configuration registers.
config_data_h = '0'*hdiff + config_data_h
config_data_l = '0'*ldiff + config_data_l

hvals = []
lvals = []

for i in range(0,19):
    hval = hex(int(config_data_h[13*i:13*i+13], 2))
    hvals.append(hval)
    lval = hex(int(config_data_l[13*i:13*i+13], 2))
    lvals.append(lval)

for i in range(0,19):
    print('    reg_mprj_io_' + str(18 - i) + ' = ' + lvals[i] + ';')

for i in range(0,19):
    print('    reg_mprj_io_' + str(19 + i) + ' = ' + hvals[i] + ';')
