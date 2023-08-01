#include "../defs.h"
//#include "../print_io.h"

// --------------------------------------------------------
// GPIO configuration test
//
// Assorted attempts to understand what's going on inside
// the GPIO serial programming shift register.
//
// It is believed that there may be timing violations
// causing a bit shift like the one on the first ChipIgnite
// chip, but probably not between every single I/O.
// --------------------------------------------------------

void clock11()
{
    reg_mprj_xfer = 0x66; reg_mprj_xfer = 0x76;
}

void clock00()
{
    reg_mprj_xfer = 0x06; reg_mprj_xfer = 0x16;
}

// --------------------------------------------------------

void clock10()
{
    reg_mprj_xfer = 0x46; reg_mprj_xfer = 0x56;
}

void clock01()
{
    reg_mprj_xfer = 0x26; reg_mprj_xfer = 0x36;
}

// --------------------------------------------------------

void load()
{
    reg_mprj_xfer = 0x06; reg_mprj_xfer = 0x0e;
    reg_mprj_xfer = 0x0e; reg_mprj_xfer = 0x06;		// Apply load
}

void main()
{
    unsigned int i, j, k;

    reg_mprj_datal = 0;
    reg_mprj_datah = 0;

    // Set I/O to the "intended" config
    reg_mprj_io_37 = 0x1809;
    reg_mprj_io_36 = 0x1809;
    reg_mprj_io_33 = 0x1809;
    reg_mprj_io_32 = 0x1809;
    reg_mprj_io_31 = 0x1809;
    reg_mprj_io_30 = 0x1809;
    reg_mprj_io_29 = 0x1809;
    reg_mprj_io_28 = 0x1809;
    reg_mprj_io_27 = 0x1809;
    reg_mprj_io_26 = 0x1809;
    reg_mprj_io_25 = 0x1809;
    reg_mprj_io_24 = 0x1809;
    reg_mprj_io_23 = 0x1809;
    reg_mprj_io_22 = 0x1809;
    reg_mprj_io_21 = 0x1809;
    reg_mprj_io_20 = 0x1809;
    reg_mprj_io_19 = 0x1809;
    reg_mprj_io_18 = 0x1809;
    reg_mprj_io_17 = 0x1809;
    reg_mprj_io_16 = 0x1809;
    reg_mprj_io_15 = 0x1809;
    reg_mprj_io_14 = 0x1809;
    reg_mprj_io_13 = 0x1809;
    reg_mprj_io_12 = 0x1809;
    reg_mprj_io_11 = 0x1809;
    reg_mprj_io_10 = 0x1809;
    reg_mprj_io_9  = 0x1809;
    reg_mprj_io_8  = 0x1809;
    reg_mprj_io_7  = 0x1809;
    reg_mprj_io_6  = 0x1809;
    reg_mprj_io_5  = 0x1809;
    reg_mprj_io_4  = 0x0403;
    reg_mprj_io_3  = 0x0403;
    reg_mprj_io_2  = 0x0403;
    reg_mprj_io_1  = 0x1809;
    reg_mprj_io_0  = 0x1809;

    // Enable GPIO (all output, ena = 0)
    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;

    // Enable bit-bang mode
    reg_mprj_xfer = 0x06;			// Enable bit-bang mode
    reg_mprj_xfer = 0x04; reg_mprj_xfer = 0x06;	// Pulse reset

    if (1) {
	// Channels 19 and 18
	clock11();
	clock11();
	clock11();
	clock11();
	clock11();
	clock11();
	clock11();
	clock11();
	clock11();
	clock11();
	clock11();
	clock01(); // 0  (affects ch. 20)

	// Channels 20 and 17
	clock01(); // 0
	clock01(); // 0
	clock01(); // 0
	clock11(); // 1
	clock11(); // 1
	clock11(); // 1
	clock11(); // 1
	clock11(); // 1
	clock11(); // 1
	clock11(); // 1
	clock11(); // 1
	clock11(); // 1

	// Channels 21 and 16	/* 21 cannot be made to work? */
	clock01();
	clock00();
	clock00();
	clock10();
	clock10();
	clock10();
	clock10();
	clock10();
	clock10();
	clock10();
	clock10();
	clock11();

	// Channels 22 and 15
	clock01(); // 0
	clock00(); // 0
	clock00(); // 0
	clock10(); // 1
	clock10(); // 1
	clock10(); // 1
	clock10(); // 1
	clock10(); // 1
	clock10(); // 1
	clock10(); // 1
	clock10();
	clock11();

	// Channels 23 and 14
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock10();
	clock11();

	// Channels 24 and 13
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock10();
	clock11();

	// Channels 25 and 12
	clock01();	/* Ch 25:  000110101011 works. . . */
	clock00();
	clock00();
	clock10();
	clock10();
	clock00();
	clock10();
	clock00();
	clock10();
	clock00();
	clock10();
	clock11();

	// Channels 26 and 11
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();

	// Channels 27 and 10
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();

	// Channels 28 and 9
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();

	// Channels 29 and 8
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();

	// Channels 30 and 7
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();

	// Channels 31 and 6
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();

	// Channels 32 and 5
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();

	// Channels 33 and 4
	clock11();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock10();

	// Channels 34 and 3
	clock10();
	clock01();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock01();
	clock11();

	// Channels 35 and 2
	clock10();
	clock01();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock01();
	clock11();

	// Channels 36 and 1
	clock10();
	clock01();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock01();
	clock11();

	// Channels 37 and 0
	// NOTE:  Channel 0 must be off or else debug mode gets enabled!
	clock10();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock11();
	clock00();
	clock01();
	clock11();

	load();
	load();
	load();
    }

    while (1) {

	// Blink forever
	// Pulse N times for channel N before the long pulse

        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;

        i = 0x20;
        for (j = 0; j < 5; j++) {
             reg_mprj_datah = i;
             for (k = 0; k < 250; k++);
                 reg_mprj_datah = 0x00000000;
             for (k = 0; k < 250; k++);
             i >>= 1;
             i |= 0x20;
        }
        i = 0x80000000;
        for (j = 0; j < 32; j++) {
             reg_mprj_datah = 0x3f;
             reg_mprj_datal = i;
             for (k = 0; k < 250; k++);
             reg_mprj_datah = 0x00;
                 reg_mprj_datal = 0x00000000;
             for (k = 0; k < 250; k++);
             i >>= 1;
             i |= 0x80000000;
        }
        reg_mprj_datal = 0xffffffff;
        reg_mprj_datah = 0x0000003f;

        reg_gpio_out = 0x1;

        for (j = 0; j < 40000; j++);

        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;

        reg_gpio_out = 0x0;

        for (j = 0; j < 40000; j++);
   }
}

