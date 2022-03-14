# Notes for chipIgnite One Silicon (2106Q)

This document provides notes specific to the chipIgnite one silicon and evaluation boards and firmware.

## Hardware

The hardware board is located under `hardware/caravel_pcb_v1`

The board requires the following modifications:
* uninstall the following components:
  * `R11` -- zero ohm resistor connecting `Tx` to `IO[4]`
  * `J7` -- enable for tri-state buffer `U4` for connecting `Rx` to `U4`
  * `U4` -- tri-state buffer `U4`
  * `R16` -- pull-up resistor on Flash SCK signal
* install a jumper between `vccd1` and `1v8` on `J18`

## Firmware

The boards have been programmed with the blink firmware example in the repo.  

Example firmware includes a make target `flash` for programing the flash on the evaluation board.  

The target uses a script `firmware/util/caravel_hkflash.py`.  In some cases, you may need to hold the reset button (jumper `SW1`) while programming the flash.
Occasionally, I've had to comment or uncomment line 144 in `caravel_hkflash.py` which affects whether to hold Caravel in reset before erasing and programming the flash.

The datasheet for Caravel with the management core configuration for chipIgnite 1 (2106Q) can be found [here](./caravel_datasheet.pdf).

Note that you should use the `defs_mpw-two-mfix.h` header file for setting the GPIO configurations.


### GPIO Configuration

By default - all GPIO (5 - 37) are set to user mode bi-directional - which means you should be able to access them from your user project area.  

If your project always sets the OEB lines high (output disabled) for GPIO that are supposed to be inputs, then the configuration should be correct for your user project on startup without applying a configuration from software.

#### Upper IO range -- IO[19] to IO[37]

If you need to configure IO from the management area, we recommend you use IOs 19 - 37.  These IOs can be configured using the firmware examples.   

GPIO configuration is done by setting the memory mapped configuration registers using the configuration values in `defs_mpw-two-mfix.h`.

> GPIO_MODE_USER_STD_INPUT_NOPULL
> GPIO_MODE_USER_STD_INPUT_PULLDOWN
> GPIO_MODE_USER_STD_INPUT_PULLUP
> GPIO_MODE_USER_STD_OUTPUT
> GPIO_MODE_USER_STD_BIDIRECTIONAL
> GPIO_MODE_USER_STD_OUT_MONITORED
> GPIO_MODE_USER_STD_ANALOG

> GPIO_MODE_MGMT_STD_INPUT_NOPULL
> GPIO_MODE_MGMT_STD_INPUT_PULLDOWN
> GPIO_MODE_MGMT_STD_INPUT_PULLUP
> GPIO_MODE_MGMT_STD_OUTPUT
> GPIO_MODE_MGMT_STD_BIDIRECTIONAL
> GPIO_MODE_MGMT_STD_OUT_MONITORED
> GPIO_MODE_MGMT_STD_ANALOG

Configuring an IO in your firmware would look like as follows...

> reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;
> reg_mprj_datal = 0;
> reg_mprj_xfer = 1;
> while (reg_mprj_xfer == 1);

To set the state of an output, you need to set the corresponding bit in the reg_mprj_datal (IO 0 to 31) or reg_mprj_datah (IO 32 to 37) register.

**Important note!  GPIOs 1 to 4 have a reversed bit for management disable that requires swapping the values for "USER" and "MGMT" for these four pins.**

If you are having difficulty programing the upper IOs, you can try providing a slower clock source (5MHz).
 This can be configured by providing a clock signal on xclk input on the board and jumpering J6.  You may need to power-cycle the board and then reset after programming and applying the slower clock.

I've also tested a replacement 5MHz oscillator that I got in - if you are interested in swapping the oscillator on the board, let me know.

#### Lower IO range -- IO[0] to IO[18]

If you would like to program the lower IOs, you need to manipulate the IO configuration bit pattern to compensate for bit slippage occuring in the shift register chain for these IOs.  

To do so, you can use a utility locate at `firmware/util/slippage.py`.  You need to change the desired IO configuration in the top of the script.  

**Note: due to the bit slippage issue, you cannot configure to adjactent IOs to be connected to the management area.**

Once you have the adjusted values, put those in your code for configuring the respective IOs.  After issuing the transfer, you need to set the memory mapped registers back to the unadjusted values you intended to configure.

### Caravel_User_Project_Analog

For project using caravel_user_project_analog, you should note the mapping of the IOs in the wrapper is different from the standard wrapper.

* IO 0 thru 13  -> standard IOs mapping to mprj_io\[13:0\] 
* IO 14 thru 24 -> bare analog pins (no ESD) mapping to io_analog\[10:0\] 
* IO 25 thru 37 -> standard IOs mapping to mprj_io\[26:14\] 

See the comments in the [user_analog_project_wrapper.v](https://github.com/efabless/caravel_user_project_analog/blob/main/verilog/rtl/user_analog_project_wrapper.v) for more details.
