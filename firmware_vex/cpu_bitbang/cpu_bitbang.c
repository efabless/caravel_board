#include <defs.h>
// #include "../print_io.h"

// --------------------------------------------------------
// GPIO configuration test
//
// Assorted attempts to understand what's going on inside
// the GPIO serial programming shift register.
//
// bitbang_flood is an update of bitbang_progression.
// The understanding is that each channel has either
// (1) a hold violation, (2) a data-dependent hold
// violation, or (3) neither ((3) has not been observed
// but is possible).
//
// bitbang_flood attempts to systematically determine
// the boundary conditions between each pair of GPIO
// control blocks.  The procedure is as follows:
//
// (1) GPIO 37 and 0 never have an error, and so they do
// not need to be checked.  GPIO 0 affects the processor
// by potentially putting it in debug mode, so keep GPIO 0
// turned off by ensuring that the low four bits are 1
// (managment controlled, input and output disabled).
// GPIO 37 is free to use for input or output.  The
// management standalone GPIO is also free to use for
// input or output.
//
// (2) Analyze each side (GPIO 1 to 18, and GPIO 19 to 36)
// independently, for simplicity.
//
// (3) At the start of each cycle, do a reset to ensure that
// the registers are all zeros.
//
// (4) Analyze each GPIO in turn, starting with the one
// closest to the processor (GPIO 1 and GPIO 36).  Apply
// sequence 1100000000001, adjusting for the effect of all
// GPIOs that come before it.  This sequence puts the GPIO
// in the state of managment control, output mode, with
// both output and input buffers enabled.
//
// (5) Clock this sequence in for the number of cycles
// known to be needed for all the GPIOs preceding it.
// Then clock an additional 12 cycles, apply load, and
// test (apply output 1 and 0 and read back each).  If
// the test is successful, then there is a simple hold
// violation at the start of the GPIO.
//
// (6) If the first test fails, then assume a data-dependent
// hold violation.  Add a 1 to the run of ones in the
// sequence (e.g., 1110000000001) and repeat, but clocking
// an additional 13 cycles instead of 12.  Repeat the test.
// If the test is successful, then there is a data-dependent
// hold violation at the start of the GPIO.
//
// Note that if any GPIO has neither a simple hold violation
// or a data-dependent hold violation, then additional
// tests will be needed.
//
// To automate the test, use GPIO 37 as input and the
// standalone GPIO as output.  The program will run as
// follows:
//
// (1) Start with the left side (GPIO 36 to 19).
// (2) Run 1st test.
// (3) If and only if the test is successful, then the LED is lit,
// the GPIO test concludes with the GPIO known to have a simple
// hold violation.
// (4) If the test is unsuccessful, then the next test checks
// for a data-dependent hold violation.
// (5) If the 2nd test is successful, then the LED is lit, and
// the GPIO test conclues with the GPIO known to have a data-
// dependent hold violation.  The program waits for a pulse on
// input GPIO 37 and then proceeds to the test.
// (6) If the 2nd test is unsuccessful, then LED is off, the
// system has an unknown condition, and the program terminates
// with the LED running at a fast blink.  If this happens, the
// program must be reworked to determine the unknown condition
// and how to test for it.
// (7) The program logs the number of clocks needed to get to
// the GPIO (12 or 13)
// (8) The program waits for a pulse on input GPIO 37 and then
// proceeds to the next GPIO (return to step 2).  If the left
// side is done, then the program continues with the right
// side.  When the left side analysis is complete, the LED
// runs with a slow blink.  When the analysis of either side is
// complete, the LED runs with a slow blink.
//
// The program will run a minimum of 19 cycles (all channels
// have simple hold violations) or a maximum of 38 cycles
// (all channels have data-dependent hold violations) per
// side.  Note that if there are more than 9 data-dependent
// hold violations on a side, then it is not possible to
// configure a GPIO for input after the 9th one, and the
// test automatically fails.  This fact may limit the yield
// and render some chips unusable.
//
// This test can in principle be automated so that the
// intended GPIO state at run-time is set up in the program,
// the analyzing routine is called and runs without requiring
// input pulses on GPIO 37, and then the program automatically
// sets up the configuration for the intended run-time state
// and returns.  This manual analysis is only used to verify
// the assumptions under which the analysis is written.
//
// --------------------------------------------------------

// --------------------------------------------------------
// Low-level bit-bang routines
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
// Load registers
// --------------------------------------------------------

void load()
{
    reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x0e; reg_mprj_xfer = 0x06;		// Apply load
}

// --------------------------------------------------------
// Enable bit-bang mode and clear registers
// --------------------------------------------------------

void clear_registers()
{
    reg_mprj_xfer = 0x06;			// Enable bit-bang mode
    reg_mprj_xfer = 0x04; reg_mprj_xfer = 0x06;	// Pulse reset
}

// --------------------------------------------------------
// Clock in an input + output configuration.  The value
// passed in "ddhold" is the number of data-dependent hold
// violations up to this point.
// --------------------------------------------------------

/* Clock in data on the left side.  Assume standard hold
 * violation, so clock in 12 times and assume that the
 * next data to be clocked will start with "1", enforced
 * by the code.
 *
 * Left side = GPIOs 37 to 19
 */

void clock_in_left_short(uint32_t ddhold)
{
    uint32_t count;
    uint32_t holds = ddhold;

    clock10();
    clock10();

    for (count = 0; count < 9; count++) {
	if (holds != 0) {
	    clock10();
	    holds--;
	}
	else
	    clock00();
    }

    clock00();
}

/* Clock in data on the right side.  Assume standard hold
 * violation, so clock in 12 times and assume that the
 * next data to be clocked will start with "1", enforced
 * by the code.
 *
 * Right side = GPIOs 0 to 18
 */

void clock_in_right_short(uint32_t ddhold)
{
    uint32_t count;
    uint32_t holds = ddhold;

    clock01();
    clock01();

    for (count = 0; count < 9; count++) {
	if (holds != 0) {
	    clock01();
	    holds--;
	}
	else
	    clock00();
    }

    clock00();
}

/* Clock in data on the left side.  Clock the normal 13 times,
 * which is correct for no hold violation or for a data-
 * dependent hold violation (for the latter, ddhold must be
 * incremented before calling the subroutine).
 *
 * Left side = GPIOs 37 to 19
 */

void clock_in_left_standard(uint32_t ddhold)
{
    uint32_t count;
    uint32_t holds = ddhold;

    clock10();
    clock10();

    for (count = 0; count < 7; count++) {
	if (holds != 0) {
	    clock10();
	    holds--;
	}
	else
	    clock00();
    }

    clock10();
    clock00();    
    clock00();
    clock10();
}

/* Clock in data on the right side.  Clock the normal 13 times,
 * which is correct for no hold violation or for a data-
 * dependent hold violation (for the latter, ddhold must be
 * incremented before calling the subroutine).
 *
 * Right side = GPIOs 0 to 18
 */

void clock_in_right_standard(uint32_t ddhold)
{
    uint32_t count;
    uint32_t holds = ddhold;

    clock11();
    clock11();

    for (count = 0; count < 7; count++) {
	if (holds != 0) {
	    clock01();
	    holds--;
	}
	else
	    clock00();
    }

    clock10();
    clock00();
    clock01();
    clock11();
}

// --------------------------------------------------------
// Clock in data for GPIO 0 and 37 (fixed) and apply load.
// --------------------------------------------------------

void clock_in_end()
{
	// Right side:  GPIO 0 configured disabled
	// Left side:  GPIO 37 configured as input
	clock11();
	clock10();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock01();
	clock00();
	clock11();
	clock11();

	load();
}

// --------------------------------------------------------
// Same as above, except that GPIO is configured as an
// output for a quick sanity check.
// --------------------------------------------------------

void clock_in_end_output()
{
	// Right side:  GPIO 0 configured disabled
	// Left side:  GPIO 37 configured as output
	clock11();
	clock10();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock00();
	clock01();
	clock00();
	clock01();
	clock11();

	load();

	reg_mprj_io_37 = 0x1809;
}

// --------------------------------------------------------
// Main program entry point
// --------------------------------------------------------

void main()
{
    unsigned int i, j, k;
    uint32_t ddhold;

    reg_mprj_datal = 0;
    reg_mprj_datah = 0;

    // Set I/O to declare all I/O as output except 0 and 37.
    // 37 is an input, and 0 is turned off.  Note that
    // register 37 as input must have the high bit set, as
    // that bit slides into the next GPIO, which needs to be
    // tested under management control.  With the output
    // disabled by the input being enabled (see housekeeping.v
    // line 785), the output mode configuration is irrelevant
    // as long as it isn't zero.

    reg_mprj_io_37 = 0x1403;
    reg_mprj_io_36 = 0x1809;
    reg_mprj_io_34 = 0x1809;
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
    reg_mprj_io_20 = 0x1801;
    reg_mprj_io_19 = 0x1801;
    reg_mprj_io_18 = 0x1801;
    reg_mprj_io_17 = 0x1801;
    reg_mprj_io_16 = 0x1801;
    reg_mprj_io_15 = 0x1801;
    reg_mprj_io_14 = 0x1801;
    reg_mprj_io_13 = 0x1801;
    reg_mprj_io_12 = 0x1801;
    reg_mprj_io_11 = 0x1801;
    reg_mprj_io_10 = 0x1801;
    reg_mprj_io_9  = 0x1801;
    reg_mprj_io_8  = 0x1801;
    reg_mprj_io_7  = 0x1801;
    reg_mprj_io_6  = 0x1801;
    reg_mprj_io_5  = 0x1801;
    reg_mprj_io_4  = 0x1801;
    reg_mprj_io_3  = 0x1801;
    reg_mprj_io_2  = 0x1801;
    reg_mprj_io_1  = 0x1801;
    reg_mprj_io_0  = 0x000b;

    // Enable GPIO (all output, ena = 0)
    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;

    ddhold = 0;

    /* Enable one of the following two blocks for right or left side
     * configuration.
     */

    while (1) {

    if (1) {
	/* First quick test. . . configure channel 36 for output */
	clear_registers();
	clock_in_left_standard(0);		// GPIO 26
	clock_in_left_standard(0);		// GPIO 27
	clock_in_left_standard(0);		// GPIO 28
	clock_in_left_standard(0);		// GPIO 29
	clock_in_left_standard(0);		// GPIO 30
	clock_in_left_standard(0);		// GPIO 31
	clock_in_left_standard(0);	    // GPIO 32
	clock_in_left_standard(0);		// GPIO 33
	clock_in_left_standard(0);		// GPIO 34
	clock_in_left_standard(0);	    // GPIO 35
	clock_in_left_standard(0);		// GPIO 36
	// clock_in_left_standard(0);		// GPIO 37
    clock_in_right_standard(0);     // GPIO 3
    clock_in_right_standard(0);     // GPIO 2
    clock_in_right_standard(0);     // GPIO 1
	clock_in_end_output();		    // GPIO 0
    }

    if (0) {
	clear_registers();
	clock_in_right_short(0);	// GPIO 2 (??)
	clock_in_right_short(0);	// GPIO 1 (??)
	clock_in_end_output();		// GPIO 0
    }


	// Blink forever
	// Pulse N+1 times for channel N before the long pulse

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