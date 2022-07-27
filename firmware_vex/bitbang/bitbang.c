#include "../defs.h"
//#include "../defs_mpw-two-mfix.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void clock(int n)
{
    for (int i=0; i < n; i++) {
            reg_mprj_xfer = 0x16;
            reg_mprj_xfer = 0x06;
    }
}

void main()
{
	int i, j, k;

    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;

    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;

    int value;

    reg_mprj_xfer = 0x66;  // enable bitbang mode

    reg_mprj_xfer = 0x76; reg_mprj_xfer = 0x66; // bit - 12
    reg_mprj_xfer = 0x76; reg_mprj_xfer = 0x06; // bit - 11
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x66;
    reg_mprj_xfer = 0x76; reg_mprj_xfer = 0x06; // bit - 3
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x16; reg_mprj_xfer = 0x66;
    reg_mprj_xfer = 0x76; reg_mprj_xfer = 0x06; // bit - 0

//    clock(13); // IO[37]

    clock(12); // IO[36]
    clock(12); // IO[35]
//    clock(12); // IO[34]

    reg_mprj_xfer = 0x0e; reg_mprj_xfer = 0x06; // load

	while (1) {
        reg_gpio_out = 1; // OFF
        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;

		for (i = 0; i < 50000; i++);

        reg_gpio_out = 0;  // ON
        reg_mprj_datah = 0x0000003f;
        reg_mprj_datal = 0xffffffff;

		for (i = 0; i < 50000; i++);

    }


}

