#include "../defs.h"
#include "../gpio_config/gpio_config_io.c"
//#include "../local_defs.h"
//#include "../stub.c"

// --------------------------------------------------------
// Firmware routines
// --------------------------------------------------------

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


/*
	IO Test:
		- Configures MPRJ lower 8-IO pins as outputs
		- Observes counter value through the MPRJ lower 8 IO pins (in the testbench)
*/

void main()
{
	/*
	IO Control Registers
	| DM     | VTRIP | SLOW  | AN_POL | AN_SEL | AN_EN | MOD_SEL | INP_DIS | HOLDH | OEB_N | MGMT_EN |
	| 3-bits | 1-bit | 1-bit | 1-bit  | 1-bit  | 1-bit | 1-bit   | 1-bit   | 1-bit | 1-bit | 1-bit   |

	Output: 0000_0110_0000_1110  (0x1808) = GPIO_MODE_USER_STD_OUTPUT
	| DM     | VTRIP | SLOW  | AN_POL | AN_SEL | AN_EN | MOD_SEL | INP_DIS | HOLDH | OEB_N | MGMT_EN |
	| 110    | 0     | 0     | 0      | 0      | 0     | 0       | 1       | 0     | 0     | 0       |


	Input: 0000_0001_0000_1111 (0x0402) = GPIO_MODE_USER_STD_INPUT_NOPULL
	| DM     | VTRIP | SLOW  | AN_POL | AN_SEL | AN_EN | MOD_SEL | INP_DIS | HOLDH | OEB_N | MGMT_EN |
	| 001    | 0     | 0     | 0      | 0      | 0     | 0       | 0       | 0     | 1     | 0       |

	*/

    // 1 input for input signal
//	reg_mprj_io_8 =   GPIO_MODE_USER_STD_INPUT_NOPULL;
	reg_mprj_io_8 =   GPIO_MODE_MGMT_STD_OUTPUT;

    // 7 outputs for segments, starting at 9
	reg_mprj_io_9 =   GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_10 =  GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_11 =  GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_12 =  GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_13 =  GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_14 =  GPIO_MODE_USER_STD_OUTPUT;
	reg_mprj_io_15 =  GPIO_MODE_USER_STD_OUTPUT;

    // digit select
	reg_mprj_io_16 =  GPIO_MODE_USER_STD_OUTPUT;

    gpio_config_io();

    // activate the project by setting the 1st bit of 2nd bank of LA
    reg_la1_iena = 0;
    reg_la1_oenb = 0;
    reg_la1_data = 1 << 1;
//    reg_la1_data = 0x02;

    // reset design with 0bit of 1st bank of LA
    reg_la0_iena = 0;
    reg_la0_oenb = 0;
    reg_la0_data = 1;
    delay(3000000);
    reg_la0_data = 0;
    delay(3000000);

    // no need for anything else as this design is free running.

    // load the correct clock frequency
    // la [1] load
    // la [13:2] new period
    reg_la0_data |= (3999 << 2) + (1 << 1);
//    reg_la0_data = 0x12;
//    reg_la0_data = 0;

    while (1) {
//        reg_mprj_datal = 0x00000100;
        blink_long();
        delay(5000);
//        reg_mprj_datal = 0x00000000;
//        delay(5);
    }

}


