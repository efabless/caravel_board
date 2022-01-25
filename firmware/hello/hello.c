//#include "../defs.h"
#include "../defs_mpw-two-mfix.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void putchar(char c)
{
	if (c == '\n')
		putchar('\r');
	reg_uart_data = c;
}

void print(const char *p)
{
	while (*p)
		putchar(*(p++));
}

void main()
{
	int i, j;

	i = 1;

    reg_mprj_io_1 = GPIO_MODE_USER_STD_BIDIRECTIONAL;  // 0x1803
    reg_mprj_io_2 = GPIO_MODE_USER_STD_INPUT_NOPULL;   // 0x0403
    reg_mprj_io_3 = GPIO_MODE_USER_STD_INPUT_NOPULL;
    reg_mprj_io_4 = GPIO_MODE_USER_STD_INPUT_NOPULL;

//    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_OUTPUT;
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
//    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_6 = GPIO_MODE_MGMT_STD_OUTPUT;

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

	reg_mprj_datal = 0x00000000;

    print("Hello!\n");
//    for (j = 0; j < 170000; j++);
//    for (j = 0; j < 10000; j++);

//	for (i = 0; i < 3000; i++) {
	while(1) {
        reg_mprj_datal = 0x00080000;
        reg_gpio_data = 0x0;

        for (j = 0; j < 3000; j++);

        reg_gpio_data = 0x1;
       	reg_mprj_datal = 0x00000000;

        for (j = 0; j < 3000; j++);

        putchar('x');

	}
}

