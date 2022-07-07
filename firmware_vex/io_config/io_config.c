#include "../defs.h"
//#include "../defs_mpw-two-mfix.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void main()
{
    int i;

    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 1;

    reg_gpio_ien = 1;
    reg_gpio_oe = 1;

	reg_gpio_out = 1;
	reg_gpio_out = 0;
    for (i = 0; i < 50000; i++);
	reg_gpio_out = 1;
    for (i = 0; i < 50000; i++);
	reg_gpio_out = 0;
    for (i = 0; i < 50000; i++);
	reg_gpio_out = 1;
    for (i = 0; i < 50000; i++);

    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;

//    reg_mprj_io_0 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_1 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_1 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_2 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_3 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_4 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_5 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_6 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_7 = GPIO_MODE_MGMT_STD_OUTPUT;

while (1) {

		for (i = 0; i < 50000; i++);
        reg_gpio_out = 1;
        reg_mprj_datal = 0x00000000;
        reg_mprj_datah = 0x00000000;

		for (i = 0; i < 50000; i++);
        reg_mprj_datal = 0xffffffff;
        reg_mprj_datah = 0x0000003f;
        reg_gpio_out = 0;

	}

}

