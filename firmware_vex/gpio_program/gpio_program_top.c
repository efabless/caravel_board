/* Test of the GPIO configuration subroutine */

#include <stdio.h>

#include "gpio_program.c"
#include "local_defs.h"

/* Define reg_mprj_io_0 to _37 as global variables rather than as
 * memory-mapped address pointers so that this top level program
 * can be run independently.
 */

#define uint16_t short

uint16_t reg_mprj_io_37;
uint16_t reg_mprj_io_36;
uint16_t reg_mprj_io_35;
uint16_t reg_mprj_io_34;
uint16_t reg_mprj_io_33;
uint16_t reg_mprj_io_32;
uint16_t reg_mprj_io_31;
uint16_t reg_mprj_io_30;
uint16_t reg_mprj_io_29;
uint16_t reg_mprj_io_28;
uint16_t reg_mprj_io_27;
uint16_t reg_mprj_io_26;
uint16_t reg_mprj_io_25;
uint16_t reg_mprj_io_24;
uint16_t reg_mprj_io_23;
uint16_t reg_mprj_io_22;
uint16_t reg_mprj_io_21;
uint16_t reg_mprj_io_20;
uint16_t reg_mprj_io_19;
uint16_t reg_mprj_io_18;
uint16_t reg_mprj_io_17;
uint16_t reg_mprj_io_16;
uint16_t reg_mprj_io_15;
uint16_t reg_mprj_io_14;
uint16_t reg_mprj_io_13;
uint16_t reg_mprj_io_12;
uint16_t reg_mprj_io_11;
uint16_t reg_mprj_io_10;
uint16_t reg_mprj_io_9;
uint16_t reg_mprj_io_8;
uint16_t reg_mprj_io_7;
uint16_t reg_mprj_io_6;
uint16_t reg_mprj_io_5;
uint16_t reg_mprj_io_4;
uint16_t reg_mprj_io_3;
uint16_t reg_mprj_io_2;
uint16_t reg_mprj_io_1;
uint16_t reg_mprj_io_0;

/* Define the transfer register so that it doesn't cause a compile error */
uint16_t reg_mprj_xfer = 0;

int main(int argc, char *argv[]) {

    /* Test configuration with GPIO 32 to 37 management output	*/
    /* and GPIO 5 to 31 management input.			*/

    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_9  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_8  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_7  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;
    reg_mprj_io_6  = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_5  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;

    /* Lowest 5 GPIOs need to be set this way in order to	*/
    /* access the housekeeping SPI at run-time.  Do not change	*/
    /* them unless absolutely necessary.			*/

    reg_mprj_io_4  = GPIO_MODE_MGMT_STD_INPUT_NOPULL; 
    reg_mprj_io_3  = GPIO_MODE_MGMT_STD_INPUT_NOPULL; 
    reg_mprj_io_2  = GPIO_MODE_MGMT_STD_INPUT_NOPULL; 
    reg_mprj_io_1  = GPIO_MODE_MGMT_STD_OUTPUT; 

    /* GPIO 0 is turned off to prevent toggling the debug pin;	*/
    /* For debug, make this an output and drive it externally	*/
    /* to ground.						*/

//    reg_mprj_io_0  = GPIO_MODE_MGMT_STD_ANALOG;
    reg_mprj_io_0  = GPIO_MODE_MGMT_STD_INPUT_NOPULL;

    /* Call the programming routine */
    gpio_program();

    /* Print out the resulting values */

    fprintf(stdout, "    reg_mprj_io_37 = 0x%04x;\n", reg_mprj_io_37);
    fprintf(stdout, "    reg_mprj_io_36 = 0x%04x;\n", reg_mprj_io_36);
    fprintf(stdout, "    reg_mprj_io_35 = 0x%04x;\n", reg_mprj_io_35);
    fprintf(stdout, "    reg_mprj_io_34 = 0x%04x;\n", reg_mprj_io_34);
    fprintf(stdout, "    reg_mprj_io_33 = 0x%04x;\n", reg_mprj_io_33);
    fprintf(stdout, "    reg_mprj_io_32 = 0x%04x;\n", reg_mprj_io_32);
    fprintf(stdout, "    reg_mprj_io_31 = 0x%04x;\n", reg_mprj_io_31);
    fprintf(stdout, "    reg_mprj_io_30 = 0x%04x;\n", reg_mprj_io_30);
    fprintf(stdout, "    reg_mprj_io_29 = 0x%04x;\n", reg_mprj_io_29);
    fprintf(stdout, "    reg_mprj_io_28 = 0x%04x;\n", reg_mprj_io_28);
    fprintf(stdout, "    reg_mprj_io_27 = 0x%04x;\n", reg_mprj_io_27);
    fprintf(stdout, "    reg_mprj_io_26 = 0x%04x;\n", reg_mprj_io_26);
    fprintf(stdout, "    reg_mprj_io_25 = 0x%04x;\n", reg_mprj_io_25);
    fprintf(stdout, "    reg_mprj_io_24 = 0x%04x;\n", reg_mprj_io_24);
    fprintf(stdout, "    reg_mprj_io_23 = 0x%04x;\n", reg_mprj_io_23);
    fprintf(stdout, "    reg_mprj_io_22 = 0x%04x;\n", reg_mprj_io_22);
    fprintf(stdout, "    reg_mprj_io_21 = 0x%04x;\n", reg_mprj_io_21);
    fprintf(stdout, "    reg_mprj_io_20 = 0x%04x;\n", reg_mprj_io_20);
    fprintf(stdout, "    reg_mprj_io_19 = 0x%04x;\n", reg_mprj_io_19);
    fprintf(stdout, "    reg_mprj_io_18 = 0x%04x;\n", reg_mprj_io_18);
    fprintf(stdout, "    reg_mprj_io_17 = 0x%04x;\n", reg_mprj_io_17);
    fprintf(stdout, "    reg_mprj_io_16 = 0x%04x;\n", reg_mprj_io_16);
    fprintf(stdout, "    reg_mprj_io_15 = 0x%04x;\n", reg_mprj_io_15);
    fprintf(stdout, "    reg_mprj_io_14 = 0x%04x;\n", reg_mprj_io_14);
    fprintf(stdout, "    reg_mprj_io_13 = 0x%04x;\n", reg_mprj_io_13);
    fprintf(stdout, "    reg_mprj_io_12 = 0x%04x;\n", reg_mprj_io_12);
    fprintf(stdout, "    reg_mprj_io_11 = 0x%04x;\n", reg_mprj_io_11);
    fprintf(stdout, "    reg_mprj_io_10 = 0x%04x;\n", reg_mprj_io_10);
    fprintf(stdout, "    reg_mprj_io_9  = 0x%04x;\n", reg_mprj_io_9);
    fprintf(stdout, "    reg_mprj_io_8  = 0x%04x;\n", reg_mprj_io_8);
    fprintf(stdout, "    reg_mprj_io_7  = 0x%04x;\n", reg_mprj_io_7);
    fprintf(stdout, "    reg_mprj_io_6  = 0x%04x;\n", reg_mprj_io_6);
    fprintf(stdout, "    reg_mprj_io_5  = 0x%04x;\n", reg_mprj_io_5);
    fprintf(stdout, "    reg_mprj_io_4  = 0x%04x;\n", reg_mprj_io_4);
    fprintf(stdout, "    reg_mprj_io_3  = 0x%04x;\n", reg_mprj_io_3);
    fprintf(stdout, "    reg_mprj_io_2  = 0x%04x;\n", reg_mprj_io_2);
    fprintf(stdout, "    reg_mprj_io_1  = 0x%04x;\n", reg_mprj_io_1);
    fprintf(stdout, "    reg_mprj_io_0  = 0x%04x;\n", reg_mprj_io_0);

    return 0;
}
