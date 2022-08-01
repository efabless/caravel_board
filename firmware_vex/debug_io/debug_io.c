#include "../defs.h"
//#include "../local_defs.h"
//#include "../stub.c"

//#include "../config_io.h"
//#include "../defs_mpw-two-mfix.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

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

#define     WAIT     100000

//void bb_mode()
//{
//    // Enable bit-bang mode
//    reg_mprj_xfer = 0x06;			// Enable bit-bang mode
//    reg_mprj_xfer = 0x02;           // Pulse reset
//    reg_mprj_xfer = 0x06;
//
//}

void clock11()
{
    reg_mprj_xfer = 0x66;
    delay(WAIT);
    reg_mprj_xfer = 0x76;
    delay(WAIT);
}

void clock00()
{
    reg_mprj_xfer = 0x06;
    delay(WAIT);
    reg_mprj_xfer = 0x16;
    delay(WAIT);
}

void clock10()
{
    reg_mprj_xfer = 0x46;
    delay(WAIT);
    reg_mprj_xfer = 0x56;
    delay(WAIT);
}

void clock01()
{
    reg_mprj_xfer = 0x26;
    delay(WAIT);
    reg_mprj_xfer = 0x36;
    delay(WAIT);
}

void load()
{
    reg_mprj_xfer = 0x06; reg_mprj_xfer = 0x0e;
    delay(WAIT);
    reg_mprj_xfer = 0x0e; reg_mprj_xfer = 0x06;		// Apply load
    delay(WAIT);
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

void blink_short() {
    const int wait=1000000;
    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;
    reg_gpio_out = 0; delay(wait); // ON
    reg_gpio_out = 1; delay(wait); // OFF
}

void blink_long() {
    const int wait=3000000;
    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;
    reg_gpio_out = 0; delay(wait); // ON
    reg_gpio_out = 1; delay(wait); // OFF
}

void set_registers() {

    reg_mprj_io_1 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_2 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_OUTPUT;

//    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;

}

void main()
{
	int i, j, k;

//    set_registers();

//    bb_mode();

    blink_short();
    blink_short();
    blink_long();

    reg_mprj_datah = 0x0000003f;
    reg_mprj_datal = 0xffffffff;

    for (i = 0; i < 5; i++)
    {
        clock11();
    }
    for (i = 0; i < 0; i++)
    {
//        clock10();
        clock01();
    }

    load();

    blink_short();
    blink_short();
    blink_long();

    delay(3000000);

    for (j = 0; j < 60; j++)
    {
//        clock10();
        clock01();
        load();
        blink_long();
    }

	while (1) {}

}

