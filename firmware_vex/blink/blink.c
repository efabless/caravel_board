#include "../defs.h"
//#include "../defs_mpw-two-mfix.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

#define reg_hk_base    (*(volatile uint32_t*)0x26000000)

void main()
{
	int i, j;
//
//	i = 1;

//    reg_mprj_io_0  = 0x0000;
//    reg_mprj_io_1  = 0x0000;
//    reg_mprj_io_2  = 0x0000;        // management output (SDI)       spi master
//    reg_mprj_io_3  = 0x0000;        // management output (SCK)       spi master
//    reg_mprj_io_4  = 0x0000;        // management output (CSB)       spi master
//    reg_mprj_io_5  = 0x0000;        // management input  (UART Rx)
//    reg_mprj_io_6  = 0x0000;        // management output (UART Tx)
//    reg_mprj_io_7  = 0x0000;        // management output
//    reg_mprj_io_8  = 0x0000;        // management output
//    reg_mprj_io_9  = 0x0000;        // management output
//    reg_mprj_io_10 = 0x0000;        // management output
//    reg_mprj_io_11 = 0x0000;        // management output
//    reg_mprj_io_12 = 0x0000;        // management output
//    reg_mprj_io_13 = 0x0000;        // management output
//    reg_mprj_io_14 = 0x0000;        // management output
//    reg_mprj_io_15 = 0x0000;        // management output
//    reg_mprj_io_16 = 0x0000;        // management output
//    reg_mprj_io_17 = 0x0000;        // management output
//    reg_mprj_io_18 = 0x0000;        // management output
//
//    reg_mprj_io_19 = 0x0000;        // management output
//    reg_mprj_io_20 = 0x0000;        // management output
//    reg_mprj_io_21 = 0x0000;        // management output
//    reg_mprj_io_22 = 0x0000;        // management output
//    reg_mprj_io_23 = 0x0000;        // management output
//    reg_mprj_io_24 = 0x0000;        // management output
//    reg_mprj_io_25 = 0x0000;        // management output
//    reg_mprj_io_26 = 0x0000;        // management output
//    reg_mprj_io_27 = 0x0000;        // management output
//    reg_mprj_io_28 = 0x0000;        // management output
//    reg_mprj_io_29 = 0x0000;        // management output
//    reg_mprj_io_30 = 0x0000;        // management output
//    reg_mprj_io_30 = 0x0000;        // management output
//    reg_mprj_io_30 = 0x0000;        // management output
//    reg_mprj_io_31 = 0x0000;        // management output
//    reg_mprj_io_32 = 0x0000;        // management output
//    reg_mprj_io_33 = 0x0000;        // management output
//    reg_mprj_io_34 = 0x0000;        // management output
//    reg_mprj_io_34 = 0x0000;        // management output
//    reg_mprj_io_35 = 0x0000;        // management output
//    reg_mprj_io_36 = 0x0000;        // management output
//    reg_mprj_io_37 = 0x0000;        // management output
//
//    reg_mprj_io_37 = 0x1809;
//    reg_mprj_io_36 = 0x1809;
//    reg_mprj_io_31 = 0x1809;
//    reg_mprj_io_0 = 0x1809;
//    reg_mprj_io_36 = 0x1fff;
////    reg_mprj_io_35 = 0x0703;   // loopback
//    reg_mprj_io_35 = 0x0403;   // loopback

    //reg_mprj_io_36 = 0x1800; // works - output
    //reg_mprj_io_35 = 0x1e01; // works - output

//    reg_mprj_io_34 = 0x0403;
//    reg_mprj_io_33 = 0x0000;
//
//    reg_mprj_datal = 0;

//    reg_mprj_xfer = 1;
//    while (reg_mprj_xfer == 1);

//    int i;
//
    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 1;

    reg_gpio_ien = 1;
    reg_gpio_oe = 1;
//
//	reg_gpio_out = 1;
//	reg_gpio_out = 0;
//    for (i = 0; i < 50000; i++);
//	reg_gpio_out = 1;
//    for (i = 0; i < 50000; i++);
//	reg_gpio_out = 0;
//    for (i = 0; i < 50000; i++);
//	reg_gpio_out = 1;
//    for (i = 0; i < 50000; i++);

    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;

	while (1) {
		for (i = 0; i < 50000; i++);
        reg_gpio_out = 1;
        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;

		for (i = 0; i < 50000; i++);
        reg_gpio_out = 0;
        reg_mprj_datah = 0x0000003f;
//        if (reg_mprj_datah & 0x00000010)  reg_gpio_out = 0;
//        if (reg_mprj_datal & 0x00000008)  reg_gpio_out = 0;
        reg_mprj_datal = 0xffffffff;
//        reg_mprj_datah = 0xffffffff;
	}


//    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;
////    reg_mprj_datal = 0x00000000;
//    reg_mprj_datal = 0xffffffff;
//    reg_mprj_datah = 0x0000003f;

//    reg_mprj_xfer = 1;
//    while (reg_mprj_xfer == 1);

//    while(1) {};

}

