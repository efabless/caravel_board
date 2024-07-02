from pyftdi.spi import SpiGpioPort

class Gpio:
    def __init__(self, raw_gpio: SpiGpioPort, mask: int=0, dir: int=0, out: int=0):
        """
        mask is the direction mask for set_direction
        dir is the initial direction value for each gpio pin as bitfield
        out is the initial output value for each gpio pin as bitfield
        """
        
        self.raw_gpio = raw_gpio
        self.mask = mask
        self.dir = dir
        self.out = out

        if mask:
            raw_gpio.set_direction(mask, dir)
            raw_gpio.write(out)
    
    def get_pin(self, index, dir=1, value=1):
        return Pin(self, index, dir, value)
    
    # For an output GPIO (by index) get its current value:
    def get_output(self, index):
        return (self.out >> index) & 1
    
    def write(self, index, value, force=False):
        if not force and self.get_output(index) == value: return

        if value:
            self.out |= (1 << index)
        else:
            self.out &= ~(1 << index)
        self.raw_gpio.write(self.out)

    # Set the direction for a given GPIO pin index (1=output, 0=input):
    def set_direction(self, index, dir=1):
        self.mask |= (1 << index)
        if dir:
            self.dir |= (1 << index)
        else:
            self.dir &= ~(1 << index)
        self.raw_gpio.set_direction(self.mask, self.dir)
        

class Pin:
    def __init__(self, gpio: Gpio, index=1, dir=1, value=1):
        self.gpio = gpio
        self.index = index

        self.gpio.set_direction(self.index, dir)

        # Force a complete write on the first write after changing the direction
        self.gpio.write(self.index, value, force=True)

    def set(self):
        self.gpio.write(self.index, 1)
    
    def toggle(self):
        self.gpio.write(self.index, 1 - self.gpio.get_output(self.index))
    
    def clear(self):
        self.gpio.write(self.index, 0)
