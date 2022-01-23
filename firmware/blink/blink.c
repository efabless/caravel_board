#include "../defs.h"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

void main()
{
	int i, j;

	i = 1;

//    reg_mprj_datal = 0;

	// Enable GPIO (all output, ena = 0)
	reg_gpio_ena = 0x0;
	reg_gpio_pu = 0x0;
	reg_gpio_pd = 0x0;
	reg_gpio_data = 0x1;

//    for (j = 0; j < 170000; j++);
//    for (j = 0; j < 10000; j++);

//	for (i = 0; i < 3000; i++) {
	while(1) {
        reg_gpio_data = 0x0;
        for (j = 0; j < 3000; j++);
        reg_gpio_data = 0x1;
        for (j = 0; j < 3000; j++);
	}
}

