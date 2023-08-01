//#include "../defs.h"
#include "../defs_mpw-two-mfix.h"
#include "../print_io.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void main()
{
	int i, j;

	i = 1;

    // Left side I/O
    reg_mprj_io_37 = 0x1808;
    reg_mprj_io_36 = 0x1808;
    reg_mprj_io_33 = 0x1808;
    reg_mprj_io_32 = 0x1808;
    reg_mprj_io_31 = 0x1808;
    reg_mprj_io_30 = 0x1808;
    reg_mprj_io_29 = 0x1808;
    reg_mprj_io_28 = 0x1808;
    reg_mprj_io_27 = 0x1808;
    reg_mprj_io_26 = 0x1808;
    reg_mprj_io_25 = 0x1808;

    // Bank from 14 to 24 does not exist on Caravan projects!

    reg_mprj_io_24 = 0x1808;
    reg_mprj_io_23 = 0x1808;
    reg_mprj_io_22 = 0x1808;
    reg_mprj_io_21 = 0x1808;
    reg_mprj_io_20 = 0x1808;
    reg_mprj_io_19 = 0x1808;


//    reg_mprj_io_18 = 0x0000;
//    reg_mprj_io_17 = 0x00c0;
//    reg_mprj_io_16 = 0x0840;
//    reg_mprj_io_15 = 0x0701;
//    reg_mprj_io_14 = 0x0100;
//    reg_mprj_io_13 = 0x1c04;
//    reg_mprj_io_12 = 0x0403;
//    reg_mprj_io_11 = 0x1010;
//    reg_mprj_io_10 = 0x100e;
//    reg_mprj_io_9  = 0x0042;
//    reg_mprj_io_8  = 0x0038;
//    reg_mprj_io_7  = 0x0108;
//    reg_mprj_io_6  = 0x00e0;
//    reg_mprj_io_5  = 0x0420;
//    reg_mprj_io_4  = 0x0240;
//    reg_mprj_io_3  = 0x0480;
//    reg_mprj_io_2  = 0x0900;
//    reg_mprj_io_1  = 0x1c01;
//    reg_mprj_io_0  = 0x1c03;

    reg_mprj_datal = 0;

    reg_mprj_xfer = 1;
    while (reg_mprj_xfer == 1);

    // Reset right side I/O after transfer to the "intended" config
//    reg_mprj_io_18 = 0x1808;
//    reg_mprj_io_17 = 0x0403;
//    reg_mprj_io_16 = 0x1808;
//    reg_mprj_io_15 = 0x0403;
//    reg_mprj_io_14 = 0x1808;
//    reg_mprj_io_13 = 0x0403;
//    reg_mprj_io_12 = 0x1808;
//    reg_mprj_io_11 = 0x0403;
//    reg_mprj_io_10 = 0x1808;
//    reg_mprj_io_9  = 0x0403;
//    reg_mprj_io_8  = 0x1808;
//    reg_mprj_io_7  = 0x0403;
//    reg_mprj_io_6  = 0x1808;
//    reg_mprj_io_5  = 0x0402;
//    reg_mprj_io_4  = 0x0403;
//    reg_mprj_io_3  = 0x0403;
//    reg_mprj_io_2  = 0x0403;
//    reg_mprj_io_1  = 0x1803;
//    reg_mprj_io_0  = 0x0403;

	// Enable GPIO (all output, ena = 0)
	reg_gpio_ena = 0x0;
	reg_gpio_pu = 0x0;
	reg_gpio_pd = 0x0;
	reg_gpio_data = 0x1;

	while(1) {

//        reg_mprj_datal = 0xaaaaaaaa;
//        reg_mprj_datah = 0xaaaaaaff;
        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;

        reg_gpio_data = 0x0;

        for (j = 0; j < 3000; j++);

//        reg_mprj_datal = 0x55555555;
//       	reg_mprj_datah = 0x55555500;
//        reg_mprj_datal = 0xffff0000;
//        reg_mprj_datal = 0x00005500;
        reg_mprj_datal = 0xffffffe0;
//        reg_mprj_datal = 0xffffffff;
        reg_mprj_datah = 0xffffffff;

        reg_gpio_data = 0x1;


        for (j = 0; j < 3000; j++);
	}

}

