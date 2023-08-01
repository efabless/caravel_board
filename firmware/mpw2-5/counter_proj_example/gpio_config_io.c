#include "gpio_config_data.c"

void delay(const int d)
{

    /* Configure timer for a single-shot countdown */
	reg_timer0_config = 0;
	reg_timer0_data = d;
    reg_timer0_config = 1;

    // Loop, waiting for value to reach zero
   reg_timer0_update = 1;  // latch current value
   while (reg_timer0_value > 0) {
           reg_timer0_update = 1;
   }

}

//#define     WAIT     100000
#define     WAIT     50000
//#define     WAIT     20000

void bb_mode()
{
    // Enable bit-bang mode
    reg_mprj_xfer = 0x06;			// Enable bit-bang mode
    reg_mprj_xfer = 0x02;           // Pulse reset
    reg_mprj_xfer = 0x06;

}

void load()
{
    reg_mprj_xfer = 0x06;
    delay(WAIT);
    reg_mprj_xfer = 0x0e; 	// Apply load
    delay(WAIT);
    reg_mprj_xfer = 0x06;
    delay(WAIT);
}

void clear_registers()
{
    // clear shift register with zeros and load before starting test
    for (int i = 0; i < 250; i++)
    {
        reg_mprj_xfer = 0x06;
        delay(WAIT);
        reg_mprj_xfer = 0x16;
        delay(WAIT);
    }
    load();
}

void gpio_config_io()
{
    int i = 1; // start offset 1, first value is n_bits
    int n_bits = config_stream[0];
//    bb_mode();
    clear_registers();
    //int n_bits = sizeof(config_stream);
    while (i < n_bits)
    {
        reg_mprj_xfer = config_stream[i];
        delay(WAIT);
        reg_mprj_xfer = config_stream[i] + 0x10;
        delay(WAIT);
        i++;
    }
    load();
}

//void *memcpy(void *dest, const void *src, int n)
//{
//    for (int i = 0; i < n; i++)
//    {
//        ((char*)dest)[i] = ((char*)src)[i];
//    }
//}

