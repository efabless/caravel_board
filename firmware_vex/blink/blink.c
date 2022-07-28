#include "../defs.h"
//#include "../local_defs.h"
//#include "../stub.c"

//#include "../config_io.h"
//#include "../defs_mpw-two-mfix.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void gpio_program();
void gpio_program_local() {

    reg_mprj_io_37 = 0x1801;
    reg_mprj_io_36 = 0x0c00;
    reg_mprj_io_35 = 0x0600;
    reg_mprj_io_34 = 0x0300;
    reg_mprj_io_33 = 0x0180;
    reg_mprj_io_32 = 0x01c0;
    reg_mprj_io_31 = 0x00c0;
    reg_mprj_io_30 = 0x0060;
    reg_mprj_io_29 = 0x0030;
    reg_mprj_io_28 = 0x0018;
    reg_mprj_io_27 = 0x000c;
    reg_mprj_io_26 = 0x0006;
    reg_mprj_io_25 = 0x1003;
    reg_mprj_io_24 = 0x1801;
    reg_mprj_io_23 = 0x0c00;
    reg_mprj_io_22 = 0x0600;
    reg_mprj_io_21 = 0x0300;
    reg_mprj_io_20 = 0x0180;
    reg_mprj_io_19 = 0x0000;
    reg_mprj_io_18 = 0x0007;
    reg_mprj_io_17 = 0x1fbf;
    reg_mprj_io_16 = 0x1f7f;
    reg_mprj_io_15 = 0x1eff;
    reg_mprj_io_14 = 0x1dff;
    reg_mprj_io_13 = 0x1bff;
    reg_mprj_io_12 = 0x17ff;
    reg_mprj_io_11 = 0x0fff;
    reg_mprj_io_10 = 0x1ffc;
    reg_mprj_io_9  = 0x1ff8;
    reg_mprj_io_8  = 0x1ff1;
    reg_mprj_io_7  = 0x1fe1;
    reg_mprj_io_6  = 0x1fe0;
    reg_mprj_io_5  = 0x1f81;
    reg_mprj_io_4  = 0x1f01;
    reg_mprj_io_3  = 0x1e01;
    reg_mprj_io_2  = 0x1c01;
    reg_mprj_io_1  = 0x1c00;
    reg_mprj_io_0  = 0x100b;

    // Initiate the serial transfer
    reg_mprj_xfer = 1;
    while (reg_mprj_xfer == 1);

    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_9  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_8  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_7  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_6  = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_5  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;

    reg_mprj_io_4  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_3  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_2  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_1  = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_0  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_0  = GPIO_MODE_MGMT_STD_ANALOG;


}

void delay(const int d)
{

    /* Configure timer for a single-shot countdown */
	reg_timer0_config = 0;
	reg_timer0_data = d;
    reg_timer0_config = 1;

    // Loop, waiting for value to reach zero
   reg_timer0_update = 1;  // latch current value
   while (reg_timer0_value > 0) {
           reg_timer0_update = 1;
   }

}

void putchar(char c)
{
	if (c == '\n')
		putchar('\r');
    while (reg_uart_txfull == 1);
	reg_uart_data = c;
}

void print(const char *p)
{
	while (*p)
		putchar(*(p++));
}

void main()
{
	int i, j, k;

    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;

//    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_9  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_8  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_7  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_6  = GPIO_MODE_MGMT_STD_OUTPUT;
////    reg_mprj_io_6  = 0x1fff;
//    reg_mprj_io_5  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//
//    /* Lowest 5 GPIOs need to be set this way in order to	*/
//    /* access the housekeeping SPI at run-time.  Do not change	*/
//    /* them unless absolutely necessary.			*/
//
//    reg_mprj_io_4  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_3  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_2  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
//    reg_mprj_io_1  = GPIO_MODE_MGMT_STD_OUTPUT;
//
//    /* GPIO 0 is turned off to prevent toggling the debug pin;	*/
//    /* For debug, make this an output and drive it externally	*/
//    /* to ground.						*/
//
//    reg_mprj_io_0  = GPIO_MODE_MGMT_STD_ANALOG;

//    gpio_program();
    gpio_program_local();

    reg_uart_enable = 1;

//    print("Hello World !!");
    putchar('x');

	while (1) {

        reg_gpio_out = 1; // OFF
        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;

		delay(8000000);

        reg_gpio_out = 0;  // ON
        reg_mprj_datah = 0x0000003f;
        reg_mprj_datal = 0xffffffff;

		delay(8000000);

    }


}

