import time

class I2C:

    def __init__(self, scl, sda):
        self.scl = scl
        self.sda = sda
        
    def _delay(self):
        time.sleep_us(100)

    def init(self):
        self.scl.on()
        self.sda.on()
        self._delay()
        
    def start(self):
        self.scl.on()
        self.sda.on()
        self._delay()
        self.sda.off()
        self._delay()
        self.scl.off()
        self._delay()
        
    def stop(self):
        self.sda.off()
        self._delay()
        self.scl.on()
        self._delay()
        self.sda.on()
        self._delay()
        
    def write_bit(self, b):
        
        if (b > 0):
            self.sda.on()
        else:
            self.sda.off()
        
        self._delay()
        self.scl.on()
        self._delay()
        self.scl.off()
        
    def read_bit(self):
        
        self.sda.on()    
        self._delay()
        self.scl.on()
        self._delay()
        
        if self.sda.value():
            b = 1
        else:
            b = 0
            
        self.scl.off()
        
        return b

    def write_byte(self, byte, start=True, stop=True):

        if start:
            self.start()

        for x in range(8):
            self.write_bit(byte & 0x80)
            byte = byte << 1
         
        ack = self.read_bit()

        if stop:
            self.stop()

        return ack

    def read_byte(self, ack=True, stop=True):

        byte = 0

        for x in range(8):
            byte = byte << 1
            byte |= self.read_bit()

        if ack:
            self.write_bit(0)
        else:
            self.write_bit(1)

        if stop:
            self.stop()

        return byte

    def send(self, addr, data):

        if self.write_byte(addr << 1, True, False):
            if self.write_byte(data, False, True):
                return True

        self.stop()
        return False

    def receive(self, addr):

        if self.write_byte(addr << 1 | 0x01, True, False):
            return self.read_byte(False, True)

        return False
