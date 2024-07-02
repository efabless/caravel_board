from io import StringIO
from pyftdi.ftdi import Ftdi

def find_ftdi():
  """
  This function allows for adding additional logic to switch
  between multiple caravel boards in the future if required or override
  which FTDI device will be used.
  """
  return find_only_ftdi()


def find_only_ftdi():
  """
  Find the only connected FTDI device.
  Only works if there is exactly one.
  """

  s = StringIO()
  Ftdi.show_devices(out=s)
  devlist = s.getvalue().splitlines()[1:-1]
  gooddevs = []
  for dev in devlist:
      url = dev.split('(')[0].strip()
      name = '(' + dev.split('(')[1]
      if name == '(Single RS232-HS)':
          gooddevs.append(url)
  if len(gooddevs) == 0:
      print('Error:  No matching FTDI devices on USB bus!')
      exit(1)
  elif len(gooddevs) > 1:
      print('Error:  Too many matching FTDI devices on USB bus!')
      Ftdi.show_devices()
      exit(1)
  else:
      print('Success: Found one matching FTDI device at ' + gooddevs[0])
      return gooddevs[0]