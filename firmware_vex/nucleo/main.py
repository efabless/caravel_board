import pyb
import io_config
# sw = pyb.Switch()
# sw.callback(io_config.run())
# io_config.run()
from nucleo_api import *
test = Test()
test.voltage = 1.6
test.powerup_sequence()
test.release_reset()