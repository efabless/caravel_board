#!/usr/bin/env python3

from caravel.hk import HKSpi

with HKSpi() as hk:
    hk.identify()