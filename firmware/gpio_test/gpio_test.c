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
    reg_spimaster_config = 0xa0ff;	// Enable, prescaler = 2,
                // connect to housekeeping SPI

    reg_spimaster_config = 0xb0ff;	// Apply stream mode
    reg_spimaster_data = 0x80;		// Write 0x80 (write mode)
    reg_spimaster_data = 0x08;		// Write 0x08 (start address)
    reg_spimaster_data = 0x03;		// DCO + PLL enable
    reg_spimaster_config = 0xa1ff;	// Release CSB (ends stream mode)

    for (j = 0; j < 3000; j++);

    reg_spimaster_config = 0xb0ff;	// Apply stream mode
    reg_spimaster_data = 0x80;		// Write 0x80 (write mode)
    reg_spimaster_data = 0x11;		// Write 0x11 (start address)
    reg_spimaster_data = 0x07;		// Write 0x07 to PLL output divider
    reg_spimaster_config = 0xa1ff;	// Release CSB (ends stream mode)

    for (j = 0; j < 3000; j++);

    reg_spimaster_config = 0xb0ff;	// Apply stream mod
    reg_spimaster_data = 0x80;		// Write 0x80 (write mode)
    reg_spimaster_data = 0x09;		// Write 0x11 (start address)
    reg_spimaster_data = 0x00;		// Write 0x00 to PLL bypass
    reg_spimaster_config = 0xa1ff;	// Release CSB (ends stream mode)

    for (j = 0; j < 3000; j++);

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

    // Bank from 14 to 24 does not exist on Caravan projects!

    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_18 = 0x07ff;
    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_OUTPUT;

    // Bank from 14 to 24 does not exist on Caravan projects!

//    reg_mprj_io_14 = 0x0c04;
//    reg_mprj_io_14 = 0x3010;
    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_12 = 0x0c07;
//    reg_mprj_io_12 = 0x3010;
//    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_11 = 0x3010;
    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_9 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_8 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_7 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_6 = 0x07ff;
    reg_mprj_io_6 = 0x0403;
    reg_mprj_io_5 = 0x0403;
//    reg_mprj_io_5 = 0x87ff;

//    reg_mprj_io_4 = GPIO_MODE_USER_STD_INPUT_NOPULL;
//    reg_mprj_io_3 = GPIO_MODE_USER_STD_INPUT_NOPULL;
//    reg_mprj_io_2 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // 0x0403
//    reg_mprj_io_1 = GPIO_MODE_USER_STD_BIDIRECTIONAL;  // 0x1803

//    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_datal = 0;

    reg_mprj_xfer = 1;
    while (reg_mprj_xfer == 1);

	// Enable GPIO (all output, ena = 0)
	reg_gpio_ena = 0x0;
	reg_gpio_pu = 0x0;
	reg_gpio_pd = 0x0;
	reg_gpio_data = 0x1;

	while(1) {
        reg_gpio_data = 0x0;
        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;
        for (j = 0; j < 3000; j++);

        reg_gpio_data = 0x1;
//        reg_mprj_datal = 0xffff0000;
        reg_mprj_datal = 0xffffffe0;
        reg_mprj_datah = 0xffffffff;
        for (j = 0; j < 3000; j++);
	}

}

