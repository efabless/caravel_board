from .find_ftdi import find_ftdi
from .gpio import Gpio
from .defs import *
from pyftdi.spi import SpiController
import time


class HKSpi:
    # Historically, each utility script has its own different GPIO8 (/UART_EN)
    # initialization state. These uart_enable_mode values retain consistency
    # with those states, to support users who might rely on this behavior:
    UART_ENABLE     = 0 # GPIO8 outputs 0
    UART_DISABLE    = 1 # GPIO8 outputs 1
    UART_DEFAULT    = 2 # GPIO8 input (floating); the board's pull up/down or J2 decides.
    # NOTE: Can also pass None to mean "do nothing", i.e. retain existing state.
    def __init__(self, ftdi_device: str=None, uart_enable_mode: int=None):
        if ftdi_device == None:
            ftdi_device = find_ftdi()
        
        self.spi = SpiController(cs_count=1)
        self.spi.configure(ftdi_device)

        self.raw_gpio = self.spi.get_gpio()
        self.gpio = Gpio(self.raw_gpio)

        #NOTE: LEDs are active-low.
        # Caravel Rev 5B board (e.g. commit 0eb8c4c) has the following mapping of:
        # - D1 = ACBUS2 = GPIO10
        # - D2 = ACBUS3 = GPIO11
        # ...but this is reversed for Rev 5A (e.g. commit 28d947e)
        # and for the so-called "Rev 6B" (5V board, e.g. for GFMPW).
        # Functionally this makes no differences;
        # it just might confuse some users looking at the board.
        # If there were a way to detect the board rev, this could reverse automatically.
        self.led1 = self.gpio.get_pin(10, value=0, dir=1)
        self.led2 = self.gpio.get_pin(11, value=0, dir=1)
        # self.mr = self.gpio.get_pin(9)

        if uart_enable_mode == self.UART_ENABLE:
            self.uart_enb = self.gpio.get_pin(8, value=0, dir=1)
        elif uart_enable_mode == self.UART_DISABLE:
            self.uart_enb = self.gpio.get_pin(8, value=1, dir=1)
        elif uart_enable_mode == self.UART_DEFAULT:
            self.uart_enb = self.gpio.get_pin(8, value=1, dir=0)
        elif uart_enable_mode is not None:
            raise ValueError(f"Invalid uart_enable_mode: {uart_enable_mode}")

        self.slave = self.spi.get_port(cs=0, freq=1E6, mode=0)

    def identify(self):
        print("Caravel data:")

        mfg = self.slave.exchange([CARAVEL_STREAM_READ, 0x01], 2)
        print("   mfg        = {:04x}".format(int.from_bytes(mfg, byteorder='big')))
        
        product = self.slave.exchange([CARAVEL_REG_READ, 0x03], 1)
        print("   product    = {:02x}".format(int.from_bytes(product, byteorder='big')))
        
        data = self.slave.exchange([CARAVEL_STREAM_READ, 0x04], 4)
        print("   project ID = {:08x}".format(int('{:032b}'.format(int.from_bytes(data, byteorder='big'))[::-1], 2)))
        print("   project ID = {:08x}".format(int.from_bytes(data, byteorder='big')))

        if int.from_bytes(mfg, byteorder='big') != 0x0456:
            print("Incorrect MFG value, expected 0x0456.")
            exit(2)

    def get_status(self):
        return int.from_bytes(self.slave.exchange([CARAVEL_PASSTHRU, CMD_READ_STATUS],1), byteorder='big')

    def print_status(self):
        print("status = 0x{:02x}".format(self.get_status()))

    def print_long_status(self):
        jedec = self.flash_read_jedec()
        if jedec[0] == int('bf', 16):
            print("changing cmd values...")
            print("status reg_1 = {}".format(hex(self.get_status())))
        else:
            print("status reg_1 = {}".format(hex(self.get_status())))
            status = self.slave.exchange([CARAVEL_PASSTHRU, 0x35], 1)
            print("status reg_2 = {}".format(hex(int.from_bytes(status, byteorder='big'))))
            # print("status = {}".format(hex(from_bytes(slave.exchange([CMD_READ_STATUS], 2)[1], byteorder='big'))))



    def is_busy(self):
        return self.get_status() & SR_WIP

    def read_reg(self, reg: int):
        return self.slave.exchange([CARAVEL_REG_READ, reg], 1)
    
    def write_reg(self, reg: int, value: int):
        self.slave.exchange([CARAVEL_REG_WRITE, reg, value])

    def read_project_id(self):
        data = self.slave.exchange([CARAVEL_STREAM_READ, 0x04], 4)
        return int('{:032b}'.format(int.from_bytes(data, byteorder='big'))[::-1], 2)




    def cpu_reset_hold(self):
        self.slave.write([CARAVEL_REG_WRITE, 0x0b, 0x01])

    def cpu_reset_release(self):
        self.slave.write([CARAVEL_REG_WRITE, 0x0b, 0x00])

    def cpu_reset_toggle(self):
        self.cpu_reset_hold()
        self.cpu_reset_release()



    def flash_reset(self):
        self.slave.write([CARAVEL_PASSTHRU, CMD_RESET_CHIP])
        self.print_status()

    def flash_read_jedec(self):
        return self.slave.exchange([CARAVEL_PASSTHRU, CMD_JEDEC_DATA], 3)
    
    def flash_identify(self):
        jedec = self.flash_read_jedec()
        print("JEDEC = {:06x}".format(int.from_bytes(jedec, byteorder='big')))

        if jedec[0:1] != bytes.fromhex('ef'):
        # if jedec[0:1] != bytes.fromhex('e6'):
            print("Winbond SRAM not found")
            exit(1)

    def flash_write_enable(self):
        self.slave.write([CARAVEL_PASSTHRU, CMD_WRITE_ENABLE])

    def flash_erase(self, wait=True, quiet=False):
        if not quiet: print("Erasing chip...")

        self.flash_write_enable()
        self.slave.write([CARAVEL_PASSTHRU, CMD_ERASE_CHIP])

        if wait:
            while (self.is_busy()):
                time.sleep(0.3)
                if not quiet: print('.', end='', flush=True)
                self.led1.toggle()

            if not quiet: print("done")
            if not quiet: self.print_status()
    



    def engage_dll(self):
        self.slave.write([CARAVEL_REG_WRITE, 0x08, 0x01])
        self.slave.write([CARAVEL_REG_WRITE, 0x09, 0x00])

    def read_dll_trim(self):
        return self.slave.exchange([CARAVEL_STREAM_READ, 0x0d], 4)
    
    def disengage_dll(self):
        self.slave.write([CARAVEL_REG_WRITE, 0x09, 0x01])
        self.slave.write([CARAVEL_REG_WRITE, 0x08, 0x00])
    
    def dco_mode(self):
        self.slave.write([CARAVEL_REG_WRITE, 0x08, 0x03])
        self.slave.write([CARAVEL_REG_WRITE, 0x09, 0x00])

    # Write the 26 bits of the DCO trim value.
    # `data` is the exact 26-bit pattern to write,
    # where 0x3fff_ffff is the maximum trim (slowest clock)
    # and   0x0000_0000 is the minimum trim (fastest clock).
    # Note that it's the "population count" of bits set to 1 that determines the trim (not
    # the binary value itself). This is known as 'thermometer code' or 'unary coding' and
    # it means there are effectively only 27 distinct values, e.g.
    # ranging from 0b0 through 0b1, 0b11, 0b111... up to 0b11_1111_1111_1111_1111_1111_1111
    def dco_trim(self, value: int):
        #NOTE: DCO trim registers are laid out in little-endian order
        # with the 0x0d register receiving bits [7:0],
        # 0x0e gets [15:8], 0x0f gets [23:16], and 0x10 gets [25:24]:
        bytes_for_regs = list(value.to_bytes(4, byteorder='little'))
        self.slave.exchange([CARAVEL_STREAM_WRITE, 0x0d] + bytes_for_regs)


    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self.spi, 'close'): self.spi.close()
        else: self.spi.terminate()
        
        return False