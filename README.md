# Caravel Board

This repo provides firmware examples, flash programming and diagnostic tools for testing
Open MPW and chipIgnite projects using Caravel.  It also provides schematics, layout and gerber files for PCB evaluation and breakout boards.

## Firmware

You will need python 3.6 or later.  

To program Caravel, connect the evaluation board using a USB micro B connector.

```bash
pip3 install pyftdi

cd firmware/blink

make clean flash
```

### Install Toolchain for Compiling Code

#### For Mac

https://github.com/riscv/homebrew-riscv

#### For Linux

https://github.com/riscv/riscv-gnu-toolchain

### Diagnostics

Makefiles in the firmware project directories use 

> firmware/util/caravel_hkflash.py 

to program the flash on the board through Caravel's housekeeping SPI interface.

> firmware/util/caravel_hkdebug.py 

provides menu-driven debug through the housekeeping SPI interface for Caravel.

## Hardware

The current evaluation board for Caravel can be found at 
> hardware/caravel_pcb_v4_FTDI

The most updated breakout board for Caravel can be found at 
> hardware/caravel_breakout_v2

- The clock is driven by X1 with a frequency of 10MHz. To drive the clock with custom frequnecy, disable X1 through J6 and use the external pin for `xclk`
- The voltage regulator U5 and U6 supply `1.8V` and `3.3V` through J8 and J9. The traces have to be cut if they are supplied externally.
- `vccd1` is connected to `1.8V` through J3. The trace has to be cut if it is supplied externally
- `vddio` is connected to `3.3V` through J5. The trace has to be cut if it is supplied externally
