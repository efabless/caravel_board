#include "../defs.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void main()
{
	int i, j;

//    reg_mprj_datal = 0;

	// Enable GPIO (all output, ena = 0)
	reg_gpio_ena = 0x0;
//	reg_gpio_pu = 0x1;
	reg_gpio_pd = 0x1;
	reg_gpio_data = 0x0;

//    for (j = 0; j < 170000; j++);
    for (j = 0; j < 35000; j++);

	while (1) {
//        reg_gpio_data = 0x0;
        for (j = 0; j < 70000; j++);
//        reg_gpio_data = 0x1;
        for (j = 0; j < 70000; j++);
	}
}

