# Caravel Board Firmware for the VexRisc-V Processor

This repo provides firmware examples, flash programming and diagnostic tools for testing
Open MPW and chipIgnite projects using Caravel on the open-source GF180mcu technology node.  It also provides 
schematics, layout and gerber files for PCB evaluation and breakout boards.

The current version of this document can be found at

https://github.com/efabless/caravel_board/blob/main/gf180/README.md

or scan the QR code...

<img src="_docs/qr-code.jpeg" alt="qr-code" style="width:200px;"/>

## Firmware

You will need python 3.6 or later.  

To program Caravel, connect the evaluation board using a USB micro B connector.

```bash
pip3 install pyftdi

cd gf180/blink

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

