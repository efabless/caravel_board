from .find_ftdi import find_ftdi
from .gpio import Gpio
from .defs import *
from pyftdi.spi import SpiController
import time


class HKSpi:
    def __init__(self, ftdi_device: str=None):
        if ftdi_device == None:
            ftdi_device = find_ftdi()
        
        self.spi = SpiController(cs_count=1)
        self.spi.configure(ftdi_device)

        self.raw_gpio = self.spi.get_gpio()
        self.gpio = Gpio(self.raw_gpio)
        self.led = self.gpio.get_pin(10, value=0)
        self.led2 = self.gpio.get_pin(11, value=0)
        # self.mr = self.gpio.get_pin(9)

        # Important, disable UART by driving UART_EN high _before_ opening SPI
        self.uart_en = self.gpio.get_pin(8)

        self.slave = self.spi.get_port(cs=0, freq=1E6, mode=0)

    def identify(self):
        print("Caravel data:")

        mfg = self.slave.exchange([CARAVEL_STREAM_READ, 0x01], 2)
        print("   mfg        = {:04x}".format(int.from_bytes(mfg, byteorder='big')))
        
        product = self.slave.exchange([CARAVEL_REG_READ, 0x03], 1)
        print("   product    = {:02x}".format(int.from_bytes(product, byteorder='big')))
        
        data = self.slave.exchange([CARAVEL_STREAM_READ, 0x04], 4)
        print("   project ID = {:08x}".format(int('{:032b}'.format(int.from_bytes(data, byteorder='big'))[::-1], 2)))
        
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
        self.slave.exchange([CARAVEL_REG_WRITE, reg, value], 1)

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
                self.led.toggle()

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

    def dco_trim(self, value: (int,int,int,int)):
        self.slave.exchange([CARAVEL_REG_WRITE, 0x0d, value[0]])
        self.slave.exchange([CARAVEL_REG_WRITE, 0x0e, value[1]])
        self.slave.exchange([CARAVEL_REG_WRITE, 0x0f, value[2]])
        self.slave.exchange([CARAVEL_REG_WRITE, 0x10, value[3]])

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self.spi, 'close'): self.spi.close()
        else: self.spi.terminate()
        
        return False