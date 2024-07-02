#!/usr/bin/env python3

import binascii
from caravel.hk import HKSpi

with HKSpi() as hk:
    hk.identify()

    k = ''

    while (k != 'q'):
        print("\n-----------------------------------\n")
        print("Select option:")
        print("  (1) read CARAVEL registers ")
        print("  (2) read CARAVEL project ID ")
        print("  (3) reset CARAVEL")
        print("  (4) reset Flash")
        print("  (5) read Flash JEDEC codes")
        print("  (6) start flash erase")
        print("  (7) check flash status")
        print("  (8) engage DLL")
        print("  (9) read DLL trim")
        print(" (10) disengage DLL")
        print(" (11) DCO mode")
        print(" (12) full trim")
        print(" (13) zero trim")
        print(" (14) set register value")
        print("  (q) quit")

        print("\n")

        k = input()

        if k == '1':
            for reg in [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11, 0x12]:
                print("reg {} = {}".format(hex(reg), binascii.hexlify(hk.read_reg(reg))))

        elif k == '2':
            print("Project ID = {:08x}".format(hk.read_project_id()))

        elif k == '3':
            # reset CARAVEL
            print("Resetting CARAVEL...")
            hk.cpu_reset_toggle()

        elif k == '4':
            # reset Flash
            print("Resetting Flash...")
            hk.flash_reset()

        elif k == '5':
            hk.cpu_reset_hold()
            print("JEDEC = {}".format(binascii.hexlify(hk.flash_read_jedec())))

        elif k == '6':
            # erase Flash
            print("Starting Flash erase...")
            hk.flash_erase(wait=False, quiet=True)

        elif k == '7':
            if hk.is_busy():
                print("Flash is busy.")
            else:
                print("Flash is NOT busy.")
            hk.print_long_status()

        elif k == '8':
            print("engaging DLL...")
            hk.engage_dll()

        elif k == '9':
            print("pll_trim = {}\n".format(binascii.hexlify(hk.read_dll_trim())))

        elif k == '10':
            print("disengaging DLL...")
            hk.disengage_dll()

        elif k == '11':
            print("Clock DCO mode...")
            hk.dco_mode()

        elif k == '12':
            print("DCO mode full trim...")
            hk.dco_trim(0x3fff_ffff)

        elif k == '13':
            print("DCO mode zero trim...")
            hk.dco_trim(0x0000_0000)

        elif k == '14':
            print("Register?")
            r = input()
            reg = int(r, 0)
            print("Value?")
            v = input()
            val = int(v, 0)
            hk.write_reg(reg, val)

        elif k == 'q':
            print("Exiting...")

        else:
            print('Selection not recognized.\n')
