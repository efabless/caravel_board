# Caravel Nucleo Hat

This directory provides a diagnostic software for characterizing timing failure patterns between GPIO pads on Caravel 
for the MPW-2, MPW-3 and related shuttles.

The diagnostic runs on a STM Nucleo development board in combination with a Caravel Hat board that hosts the Caravel 
part under test.

## Setup

###Components
- NUCLEO-F746ZG or NUCLEO-F413ZH
- Caravel Nucleo Hat
- One or more Caravel breakout boards with a Caravel part installed
- receptical connector sockets for the Nucleo board
  - for connectors CN11 and CN12 
  - SAMTEC P/N SSQ-135-23-G-D
- double-row pin headers for the Caravel Nucleo Hat
- two 3-pin headers for J8 & J9 with jumpers
- package of flexy pins
- USB micro-B to USB-A cable

###Configuration
- Install the flexy pins on in the Nucleo Hat
  - see demonstration video (https://youtu.be/thXuYkltXbo)
- Install the sockets on the Nucleo board 
- Install the double-row headers and 3-pin headers on Caravel Nucleo Hat
- Install the jumpers on J8 and J9 for 'HAT'
- Plug the Caravel Nucleo Hat in Nucleo board sockets
- Install a Caravel Breakout board into the socket on the Caravel Hat board
- Connect the USB to a workstation / laptop
- Clone the github repo https://github.com/efabless/caravel_board.git
- Change to the firmware_vex/nucleo directory
- run 'pip install mpremote'

To run the diagnostic

```bash
git clone https://github.com/efabless/caravel_board.git

cd caravel_board/firmware_vex/nucleo

pip3 install mpremote

cd firmware_vex/nucleo

make run
```

If the test passes successfully for the part, run the following to retrieve the configuration file

```bash
make get_config
```

## Using the Configuration File

... coming soon