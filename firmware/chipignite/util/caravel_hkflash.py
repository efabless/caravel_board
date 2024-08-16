#!/usr/bin/env python3

import time
import sys, os
import binascii
from caravel.defs import *
from caravel.hk import HKSpi


if len(sys.argv) < 2:
   print("Usage: caravel_hkflash.py <file>")
   sys.exit()

file_path = sys.argv[1]

if not os.path.isfile(file_path):
   print("File not found.")
   sys.exit()



with HKSpi(uart_enable_mode=HKSpi.UART_DISABLE) as hk:
    hk.identify()
    hk.cpu_reset_hold()

    time.sleep(0.5)
    hk.led1.toggle()

    print(" ")
    print("Resetting Flash...")
    hk.flash_reset()
    hk.flash_identify()
    hk.flash_erase()



    buf = bytearray()
    addr = 0
    nbytes = 0
    total_bytes = 0

    with open(file_path, mode='r') as f:
        x = f.readline()
        while x != '':
            if x[0] == '@':
                addr = int(x[1:],16)
                print('setting address to {}'.format(hex(addr)))
            else:
                # print(x)
                values = bytearray.fromhex(x[0:len(x)-1])
                buf[nbytes:nbytes] = values
                nbytes += len(values)
                # print(binascii.hexlify(values))

            x = f.readline()

            if nbytes >= 256 or (x != '' and x[0] == '@' and nbytes > 0):
                total_bytes += nbytes
                # print('\n----------------------\n')
                # print(binascii.hexlify(buf))
                # print("\ntotal_bytes = {}".format(total_bytes))

                hk.flash_write_enable()
                wcmd = bytearray((CARAVEL_PASSTHRU, CMD_PROGRAM_PAGE,(addr >> 16) & 0xff, (addr >> 8) & 0xff, addr & 0xff))
                # wcmd = bytearray((CARAVEL_PASSTHRU, CMD_WRITE_ENABLE, CMD_PROGRAM_PAGE,(addr >> 16) & 0xff, (addr >> 8) & 0xff, addr & 0xff))
                # print(binascii.hexlify(wcmd))
                # wcmd.extend(buf[0:255])
                wcmd.extend(buf)
                hk.slave.exchange(wcmd)
                while (hk.is_busy()):
                    time.sleep(0.1)

                print("addr {}: flash page write successful".format(hex(addr)))

                if nbytes > 256:
                    buf = buf[255:]
                    addr += 256
                    nbytes -= 256
                    print("*** over 256 hit")
                else:
                    buf = bytearray()
                    addr += 256
                    nbytes =0

        if nbytes > 0:
            total_bytes += nbytes
            # print('\n----------------------\n')
            # print(binascii.hexlify(buf))
            # print("\nnbytes = {}".format(nbytes))

            hk.flash_write_enable()
            wcmd = bytearray((CARAVEL_PASSTHRU, CMD_PROGRAM_PAGE, (addr >> 16) & 0xff, (addr >> 8) & 0xff, addr & 0xff))
            # wcmd = bytearray((CARAVEL_PASSTHRU, CMD_WRITE_ENABLE, CMD_PROGRAM_PAGE, (addr >> 16) & 0xff, (addr >> 8) & 0xff, addr & 0xff))
            wcmd.extend(buf)
            hk.slave.exchange(wcmd)
            while (hk.is_busy()):
                time.sleep(0.1)

            print("addr {}: flash page write successful".format(hex(addr)))

    print("\ntotal_bytes = {}".format(total_bytes))

    hk.print_long_status()

    print("************************************")
    print("verifying...")
    print("************************************")

    buf = bytearray()
    addr = 0
    nbytes = 0
    total_bytes = 0

    while (hk.is_busy()):
        time.sleep(0.5)

    # slave.write([CARAVEL_REG_WRITE, 0x0b, 0x01])
    # slave.write([CARAVEL_REG_WRITE, 0x0b, 0x00])

    hk.print_long_status()

    with open(file_path, mode='r') as f:
        x = f.readline()
        while x != '':
            if x[0] == '@':
                addr = int(x[1:],16)
                print('setting address to {}'.format(hex(addr)))
            else:
                # print(x)
                values = bytearray.fromhex(x[0:len(x)-1])
                buf[nbytes:nbytes] = values
                nbytes += len(values)
                # print(binascii.hexlify(values))

            x = f.readline()

            if nbytes >= 256 or (x != '' and x[0] == '@' and nbytes > 0):

                total_bytes += nbytes
                # print('\n----------------------\n')
                # print(binascii.hexlify(buf))
                # print("\ntotal_bytes = {}".format(total_bytes))

                read_cmd = bytearray((CARAVEL_PASSTHRU, CMD_READ_LO_SPEED,(addr >> 16) & 0xff, (addr >> 8) & 0xff, addr & 0xff))
                # print(binascii.hexlify(read_cmd))
                buf2 = hk.slave.exchange(read_cmd, nbytes)
                if buf == buf2:
                    print("addr {}: read compare successful".format(hex(addr)))
                else:
                    print("addr {}: *** read compare FAILED ***".format(hex(addr)))
                    print(binascii.hexlify(buf))
                    print("<----->")
                    print(binascii.hexlify(buf2))

                if nbytes > 256:
                    buf = buf[255:]
                    addr += 256
                    nbytes -= 256
                    print("*** over 256 hit")
                else:
                    buf = bytearray()
                    addr += 256
                    nbytes =0

        if nbytes > 0:
            total_bytes += nbytes
            # print('\n----------------------\n')
            # print(binascii.hexlify(buf))
            # print("\nnbytes = {}".format(nbytes))

            read_cmd = bytearray((CARAVEL_PASSTHRU, CMD_READ_LO_SPEED, (addr >> 16) & 0xff, (addr >> 8) & 0xff, addr & 0xff))
            # print(binascii.hexlify(read_cmd))
            buf2 = hk.slave.exchange(read_cmd, nbytes)
            if buf == buf2:
                print("addr {}: read compare successful".format(hex(addr)))
            else:
                print("addr {}: *** read compare FAILED ***".format(hex(addr)))
                print(binascii.hexlify(buf))
                print("<----->")
                print(binascii.hexlify(buf2))

    print("\ntotal_bytes = {}".format(total_bytes))

    print("pll_trim = {}\n".format(binascii.hexlify(hk.read_dll_trim())))

    # print("Setting trim values...\n")
    # slave.write([CARAVEL_REG_WRITE, 0x04, 0x7f])

    # pll_trim = slave.exchange([CARAVEL_REG_READ, 0x04],1)
    # print("pll_trim = {}\n".format(binascii.hexlify(pll_trim)))

    hk.cpu_reset_release()

    hk.led1.toggle()
    time.sleep(0.3)
    hk.led1.toggle()

