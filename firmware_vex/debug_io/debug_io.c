#include "../defs.h"
#include "../gpio_config/gpio_config_io.c"
//#include "../local_defs.h"
//#include "../stub.c"

//#include "../config_io.h"
//#include "../defs_mpw-two-mfix.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

//void delay(const int d)
//{
//
//    /* Configure timer for a single-shot countdown */
//	reg_timer0_config = 0;
//	reg_timer0_data = d;
//    reg_timer0_config = 1;
//
//    // Loop, waiting for value to reach zero
//   reg_timer0_update = 1;  // latch current value
//   while (reg_timer0_value > 0) {
//           reg_timer0_update = 1;
//   }
//
//}
//
////#define     WAIT     100000
//#define     WAIT     50000
////#define     WAIT     20000


//void clock11()
//{
//    reg_mprj_xfer = 0x66;
//    delay(WAIT);
//    reg_mprj_xfer = 0x76;
//    delay(WAIT);
//}

void clock00()
{
    reg_mprj_xfer = 0x06;
    delay(WAIT);
    reg_mprj_xfer = 0x16;
    delay(WAIT);
}

//void clock10()
//{
//    reg_mprj_xfer = 0x46;
//    delay(WAIT);
//    reg_mprj_xfer = 0x56;
//    delay(WAIT);
//}
//
//void clock01()
//{
//    reg_mprj_xfer = 0x26;
//    delay(WAIT);
//    reg_mprj_xfer = 0x36;
//    delay(WAIT);
//}

//void load()
//{
//    reg_mprj_xfer = 0x06;
//    delay(WAIT);
//    reg_mprj_xfer = 0x0e; 	// Apply load
//    delay(WAIT);
//    reg_mprj_xfer = 0x06;
//    delay(WAIT);
//}

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

    reg_mprj_io_0 = GPIO_MODE_MGMT_STD_ANALOG;
    reg_mprj_io_1 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_2 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_3 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_4 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_5 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_6 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_7 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_8 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_9 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_34 = 0x0403;
    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_37 = 0x0403;

}

//void clock_short()
//{
//        // clock an 0x1801 pattern based an a data-independent hold
//        clock11();
//        clock11();
//        clock01();
//        clock01();
//        clock01();
//        clock01();
//        clock01();
//        clock01();
//        clock01();
//        clock01();
//        clock01();
//        clock01();
////        clock11();
//}

//int gpio_reg = {
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//    0b1100000000001,
//};

void main()
{
	int i, j, k;

    set_registers();

//    bb_mode();

    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;
    reg_gpio_out = 1; // OFF

    blink_short();
    blink_short();
    blink_long();

    reg_mprj_datah = 0x0000003f;
//    reg_mprj_datah = 0x00000000;
//    reg_mprj_datah = 0x0000002f;
    reg_mprj_datal = 0xffffffff;

//    // clear shift register with zeros and load before starting test
//    for (i = 0; i < 250; i++)
//    {
//        clock00();
//    }
//
//    load();
//
//    blink_short();
//    blink_short();
//    blink_long();

    gpio_config_io();

    blink_short();
    blink_short();
    blink_long();
    blink_long();

    delay(6000000);

	while (1) {
	    reg_mprj_datal = 0x0000001;  reg_mprj_datah = 0x0000000;
//	    reg_mprj_datal = 0xffffffff;
//	    reg_gpio_out = ~ (reg_mprj_datah  >> 5);
//	    reg_gpio_out = ~ (reg_mprj_datah  >> 2);
//        delay(1000000);
        blink_long();
	    reg_mprj_datal = 0xffffffff;  reg_mprj_datah = 0x0000003f;
//        delay(3000000);
//        reg_mprj_datah = 0x0000002f;
//        blink_long();
        delay(3000000);
//        reg_mprj_datah = 0x0000003f;
	}

}

