//#include "../defs.h"
#include "../defs_mpw-two-mfix.h"
#include "../print_io.h"
//#include "spi_io.h"


// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void set_gpio(int pin)
{
    (volatile uint32_t) ((reg_mprj_datal) |= pin);
}

void clear_gpio(int pin)
{
    (volatile uint32_t) ((reg_mprj_datal) &= ~(pin));
}

void main()
{
	int i, j, k;

	i = 1;

//    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;
//
//    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_OUTPUT;
//
//    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_OUTPUT;
//
//    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;
//
//    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_OUTPUT;
//
//    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_9 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_8 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_7 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_6 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_5 = GPIO_MODE_MGMT_STD_OUTPUT;
//
//    reg_mprj_io_4 = GPIO_MODE_USER_STD_INPUT_NOPULL;
//    reg_mprj_io_3 = GPIO_MODE_USER_STD_INPUT_NOPULL;
//    reg_mprj_io_2 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // 0x0403
//    reg_mprj_io_1 = GPIO_MODE_USER_STD_BIDIRECTIONAL;  // 0x1803

    reg_mprj_io_6 = 0x7ff;

    reg_mprj_datal = 0;

    reg_uart_clkdiv = 1042;
    reg_uart_enable = 1;

    reg_mprj_xfer = 1;
    while (reg_mprj_xfer == 1);

	// Enable GPIO (all output, ena = 0)
	reg_gpio_ena = 0x0;
	reg_gpio_pu = 0x0;
	reg_gpio_pd = 0x0;
	reg_gpio_data = 0x1;

    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_9 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_8 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_7 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_6 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_5 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_4 = GPIO_MODE_USER_STD_INPUT_NOPULL;
    reg_mprj_io_3 = GPIO_MODE_USER_STD_INPUT_NOPULL;
    reg_mprj_io_2 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // 0x0403
    reg_mprj_io_1 = GPIO_MODE_USER_STD_BIDIRECTIONAL;  // 0x1803

//	reg_mprj_datal = 0x00000000;
//	reg_mprj_datah = 0x00000000;

//    spi_init();

//    print("Hello!\n");

    char *msg[] = {
//  "******************* ",
    " Woowzaaa!!         ",
    "                    ",
    " I'm Caravel !!     ",
    "      I'm Alive !!! ",
//  "******************* ",
    };

    int n = 4;

    putchar("|"); putchar(0x80);
    putchar("|"); putchar(0x9e);
    putchar("|"); putchar(0xbc);

	while(1) {
	    print("|"); putchar(0x2d); // clear screen

        for (i=0; i < 2; i++) {
            reg_gpio_data = 0x0;
            for (j = 0; j < 3000; j++);
            reg_gpio_data = 0x1;
            for (j = 0; j < 5000; j++);
        }

	    for (i = 0; i < n; i++) {
	        print(msg[i]);
	        for (j = 0; j < 5000; j++);
	        reg_gpio_data = 0x0;
            for (j = 0; j < 5000; j++);
	        reg_gpio_data = 0x1;
	    }

        for (j = 0; j < 10000; j++);

//        for (i=0; i < 2; i++) {
//            reg_gpio_data = 0x0;
//            for (j = 0; j < 3000; j++);
//            reg_gpio_data = 0x1;
//            for (j = 0; j < 5000; j++);
//        }

//        i = 0;
//        while (i < 38) {
//            for (j = i; j < i+4; j++) {
////                print("|"); putchar(0x2d); // clear screen
//                print_dec(j); print(" : 0x"); print_hex(reg_mprj_io_0 + j*4, 4); print("\n");
////                print_dec(j); print(" : 0x"); print_hex(reg_mprj_io_0 + j*4, 4); print("\n");
////                print_dec(j); print(" : 0x"); print_hex(reg_mprj_io_0 + j*4, 4); print("\n");
//                for (k = 0; k < 10000; k++);
//            }
//            i += 4;
//        }
//
//        for (j = 0; j < 30000; j++);

    }

//        reg_mprj_datal = 0x00080000;
//        reg_mprj_datal = 0xffffffff;
//        reg_mprj_datah = 0xffffffff;
//        set_gpio(19);
//        reg_gpio_data = 0x0;
//
//        for (j = 0; j < 3000; j++);
//
////       	reg_mprj_datal = 0x00000000;
////       	reg_mprj_datah = 0x00000000;
////        clear_gpio(19);
//        reg_gpio_data = 0x1;
//
//        for (j = 0; j < 3000; j++);

//        putchar('x');

//	}
}

