#include "../defs.h"
#include "../gpio_config/gpio_config_io.c"
//#include "../stub.c"
#include "../print_io.c"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void set_registers() {
    // Left side I/O
    reg_mprj_io_37 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_33 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_32 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_31 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_30 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_29 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_28 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_27 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_26 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_25 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_24 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_23 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_22 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_21 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_20 = GPIO_MODE_USER_STD_OUTPUT;
    reg_mprj_io_19 = GPIO_MODE_USER_STD_OUTPUT;

    // Right side I/O
	reg_mprj_io_18 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_17 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_16 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_15 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_14 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_13 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_12 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_11 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_10 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_9 =   GPIO_MODE_USER_STD_OUTPUT;

	reg_mprj_io_8 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_7 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_6 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_5 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_4 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_3 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_2 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_1 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_0 =   GPIO_MODE_USER_STD_OUTPUT;
}

void main()
{

    gpio_config_io();

    set_registers();

	reg_gpio_out = 1; // OFF
    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;

	// Configure All LA probes as inputs to the cpu
	reg_la0_oenb = reg_la0_iena = 0x00000000;    // [31:0]
	reg_la1_oenb = reg_la1_iena = 0x00000000;    // [63:32]
	reg_la2_oenb = reg_la2_iena = 0x00000000;    // [95:64]
	reg_la3_oenb = reg_la3_iena = 0x00000000;    // [127:96]

	// Configure LA[64] LA[65] as outputs from the cpu
	reg_la2_oenb = reg_la2_iena = 0x00000003;

	// Set clk & reset to one
	reg_la2_data = 0x00000003;

    delay(1000000);

	// De-assert reset
	reg_la2_data = 0x00000000;

//    const int COUNT_DELAY = 2000;
//    const COUNT_DELAY = 300000;
    const int COUNT_DELAY = 1000000;

	while(1) {

        reg_gpio_out = 0x0;  // LED on

		reg_la2_data = 0x00000001; // pulse clk

        delay(COUNT_DELAY);

        reg_gpio_out = 0x1;   // LED off

		reg_la2_data = 0x00000000;  // pulse clk

        delay(COUNT_DELAY);

	}

}

