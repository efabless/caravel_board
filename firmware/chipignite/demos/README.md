# Caravel Demos

Demonstrations of interacting with Caravel. Resources:

* Caravel harness documentation https://caravel-harness.readthedocs.io/en/latest/index.html
* Caravel SoC documentation https://caravel-mgmt-soc-litex.readthedocs.io/en/latest/ 
* Demo PCB files: https://github.com/efabless/caravel_board/tree/main/hardware/development/caravel-dev-v5-M.2
* GCC Toolchain installation: https://github.com/efabless/caravel_board/main/demos#install-toolchain-for-compiling-code

## HKDebug demos

### Read the project ID from the commandline

caravel_hkdebug.py is a tool that can interact with Caravel via the [housekeeping spi (HKSPI)](https://caravel-harness.readthedocs.io/en/latest/housekeeping-spi.html#housekeeping-spi-registers).

Start caravel_hkdebug.py:

	make hk_debug

Then type `2` to get the project ID.

### Reboot Caravel from the commandline

Start caravel_hkdebug.py:

	make hk_debug

Then type `3` to get the project ID.

### DLL (PLL) enable / disable from commandline

*Note: The naming is confusing as the DLL is referred to as both DLL and PLL. DLL is more correct, but PLL is still in use for firmware register names.*

Start caravel_hkdebug.py:

	make hk_debug

Then type `8` to enable the DLL. The LED should start flashing 4 times faster.
Type `10` to disable the DLL.

### Change DLL frequency from the commandline

This [calculator](https://github.com/kbeckmann/caravel-pll-calculator) makes it easy to list DLL frequencies and get the
required register values.

The onboard oscillator is 10MHz, and the maximum internal frequency supported by the DLL is around 100MHz.
After cloning the calculator you can run it like this:

    caravel_pll.py  list --clkin 10 --pll-high 100

To get a list of possible DLL frequencies. To get the register values for a specific frequency, use it like this:

    caravel_pll.py generate --clkin 10 --pll-high 100 --clkout 30

This results in register `0x11: 0x1b` and register `0x12: 0x09`. To set these on the commandline, start caravel_hkdebug.py:

	make hk_debug

Then type `14` to set a register, choose register `0x11` and give `0x1b`. Then repeat for register `0x12` with value `0x09`.
Finally enable the DLL by typing `8`.

## Firmware demos

### Flash the firmware

Check the top lines of the [Makefile](Makefile). If your RISCV compiler is installed in a different location you will need
to either edit the Makefile to update the `TOOLCHAIN_PATH` or set it on the commandline each time you start a new session:

    export TOOLCHAIN_PATH=/opt/bin/your/path

Then you should be able to compile the firmware with:

    make

If it works, you will get a firmware hex file called `demos.hex` in your directory. If not, check the errors and make sure your 
paths and environment variables are correct. If you get stuck try the `#mpw-6plus-silicon` channel in the [open source silicon slack](https://join.slack.com/t/open-source-silicon/shared_invite/zt-1s2swn9it-F_qblosmmeHmyY~BtG6BfA).

To flash it, type:

    make flash
    
That should result in a log like this:

    python3 ../util/caravel_hkflash.py demos.hex                  
    Success: Found one matching FTDI device at ftdi://ftdi:232h:1:67/1                                                                       
                                                                  
    Caravel data:                                                 
       mfg        = 0456                                          
       product    = 11                                            
       project ID = 2206ff36                                      
                                                                  
    Resetting Flash...                                            
    status = 0x00                                                 
                                                                  
    JEDEC = b'ef4016'                                             
    Erasing chip...                                               
    done                                                          
    status = 0x0                                                  
    setting address to 0x0                                        
    addr 0x0: flash page write successful                         
    addr 0x100: flash page write successful                       
    addr 0x200: flash page write successful                       
    addr 0x300: flash page write successful                             
    addr 0x400: flash page write successful                       
    addr 0x500: flash page write successful                       
    addr 0x600: flash page write successful                       
    addr 0x700: flash page write successful                       
    addr 0x800: flash page write successful                       
    addr 0x900: flash page write successful                       
    addr 0xa00: flash page write successful                       
    addr 0xb00: flash page write successful                       
    addr 0xc00: flash page write successful                       
    addr 0xd00: flash page write successful                       
    addr 0xe00: flash page write successful                       
    setting address to 0xf00                                      
    addr 0xf00: flash page write successful                       
                                                                  
    total_bytes = 4096                                            
    status reg_1 = 0x0                                            
    status reg_2 = 0x2                                            
    ************************************                          
    verifying...                                                  
    ************************************                          
    status reg_1 = 0x0                                            
    status reg_2 = 0x2                                            
    setting address to 0x0                                        
    addr 0x0: read compare successful                             
    addr 0x100: read compare successful                           
    addr 0x200: read compare successful                                 
    addr 0x300: read compare successful                                 
    addr 0x400: read compare successful                                 
    addr 0x500: read compare successful                                 
    addr 0x600: read compare successful                                 
    addr 0x700: read compare successful                                 
    addr 0x800: read compare successful                                 
    addr 0x900: read compare successful                                 
    addr 0xa00: read compare successful                                 
    addr 0xb00: read compare successful                                 
    addr 0xc00: read compare successful                                 
    addr 0xd00: read compare successful                                 
    addr 0xe00: read compare successful                                 
    setting address to 0xf00                                            
    addr 0xf00: read compare successful                                 

    total_bytes = 4096                                                  
    pll_trim = b'6c'                               

And the red GPIO LED should start flashing on the demo board. If you get an error then:

* Check the board is connected properly
* List the FTDI devices with `lsftdi`, it should show as `Manufacturer: FTDI, Description: FT232R USB UART`
* Check you have permissions. The serial device will often be owned by `plugdev` or `dialout`. You can try these [instructions](https://askubuntu.com/questions/112568/how-do-i-allow-a-non-default-user-to-use-serial-device-ttyusb0) to fix it.
* Check the M2 breakout board is properly inserted into the board.
* If you get stuck then ask for help in the `#mpw-6plus-silicon` channel of the slack.

### GPIO demo

The demo you just flashed sets up the GPIOs to be 'management controlled'. This means the RISCV coprocessor controls the IOs, not the user design.

GPIOs must be setup before use - see the `configure_io` function. After setting all the values, you must update the GPIOs with this code:

    reg_mprj_xfer = 1;
    while (reg_mprj_xfer == 1);

As there are 37 GPIOs, there are 2 sets of 32bit registers you can use to read and write them:

    # write to all bits
    reg_mprj_datal = 0x00000000;
    reg_mprj_datah = 0x00000000;

    # read from all bits
    data0 = reg_mrpj_datal;
    data1 = reg_mrpj_datah;

### Set the DLL in firmware

To set the DLL with firmware, we need to write to 4 registers: `pll_source` and `pll_divider` to set the frequency, then enable it with `pll_ena` and finally switch the core from the external oscillator to the DLL with `pll_bypass`.

    reg_hkspi_pll_source  = 0x1b;   // default 0x12
    reg_hkspi_pll_divider = 0x09;   // default 0x04
    reg_hkspi_pll_ena     = 1;      // default 0x00 
    reg_hkspi_pll_bypass  = 0;      // default 0x01
    reg_clk_out_dest      = 2;      // monitor the user clock on GPIO[15]

Edit the [demos.c](demos.c) file and enable the DLL by uncommenting `#define DLL_DEMO` at the top of the file.

Make sure the DLL is [currently not activated](#dll-pll-enable--disable-from-commandline) and then flash the firmware.

    make flash

After the firmware has flashed, you should see the LED blinking faster. The user clock should also be output on GPIO15 if you want to measure it.
With the values given, it should be 30MHz.

### Serial communication

Caravel has a serial uart, connected to the FTDI chip. However, the FTDI is used to program the HKSPI, so it can't be used to read and write serial to Caravel without putting a jumper on J2.
This will then prevent flashing new firmware. So either remove the jumper to flash, then replace it, or use another USB to serial adapter on pins 5 & 6.

To try this demo, first uncomment `#ifdef SERIAL_DEMO` and comment *all the other* demo defines. Flash the firmware as usual, then place a jumper on J2.

Now start `miniterm.py` by running 

    make monitor

You may need to edit the Makefile to change the serial port used. Press any key to get the menu:

    --- Miniterm on /dev/serial/by-id/usb-FTDI_Single_RS232-HS-if00-port0  9600,8,N,1 ---
    --- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
    a: hello
    b: count
    c: blink

* Pressing `a` should print back `Hello World !!`.
* Pressing `b` should increment a counter and print the result. 
* Pressing `c` should blink all the GPIOs once.

If you don't see anything then check J2 is correctly placed and your serial port is the right one. 
If you see bad characters, then the DLL is probably activated and you need to disable it.


### Wishbone and Logic Analyser

Unfortunately it's not possible to make a universal demo for Wishbone (WB) or Logic Analyser (LA) because they depend on the user project on the chip.

This demo uses a [shared SRAM](https://docs.google.com/document/d/1wLjU6hkAoYvSWNBAyTj8HmIV70eJWU3apa9_OEpsd3Y/edit#heading=h.d6kk3xet6rfq) taped out on 
the [Zero to ASIC course's group submission to MPW6](https://zerotoasiccourse.com/post/mpw6_submitted/).

The LA is used to enable and configure the SRAM, and then WB is used to write and then read the SRAM.

The serial port is also used to print the memory contents. If you have this chip then you can try the demo by:

* uncomment the `#ifdef WB_LA_DEMO`
* flash the firmware
* place J2 for serial
* start the serial monitor
* reset Caravel

The result should be the following:

    --- Miniterm on /dev/serial/by-id/usb-FTDI_Single_RS232-HS-if00-port0  9600,8,N,1 ---
    --- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
    0000
    0001
    0002
    0003
    0004
    0005
    0006
    0007
    0008
    0009
    000a
    000b
    000c
    000d
    000e
    000f

### Wishbone notes

* You must enable WB with `reg_wb_enable  = 1;`. 
* You can read and write to memory addresses above 0x3000_0000.

### Logic Analyser notes

The 128 bit wide LA has 4 banks, each with 4 sets of 32 bit registers to control it.

* `reg_la0_oenb`, set low to enable the output
* `reg_la0_iena`, set low to enable the input
* `reg_la0_data`, write to this register to put data on the LA
* `reg_la0_data_in`, read from this register to fetch data from the LA
