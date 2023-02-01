#include "../defs.h"
#include "gpio_config_io.c"
#include "send_packet.c"
//#include "../local_defs.h"
//#include "../stub.c"

//#include "../config_io.h"
//#include "../defs_mpw-two-mfix.h"

void set_registers() {

    reg_mprj_io_0 = GPIO_MODE_MGMT_STD_ANALOG;
    reg_mprj_io_1 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_2 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_3 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_4 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_5 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_6 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_7 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_8 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_9 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_10 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_11 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_12 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_13 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_14 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_15 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_16 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_17 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_18 = GPIO_MODE_MGMT_STD_OUTPUT;

    reg_mprj_io_19 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_20 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_21 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_22 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_23 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_24 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_25 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_26 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_27 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_28 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_29 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_30 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_31 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_32 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_33 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_34 = GPIO_MODE_MGMT_STD_OUTPUT;
//    reg_mprj_io_34 = 0x0403;
    reg_mprj_io_35 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_36 = GPIO_MODE_MGMT_STD_OUTPUT;
    reg_mprj_io_37 = GPIO_MODE_MGMT_STD_INPUT_PULLDOWN;
//    reg_mprj_io_37 = 0x0403;

}
/*

@ start of test  after configuration
    send packet with size = 1
@ send 4 pulses at gpio[0]  
    send packet with size = 2
@ send 4 pulses at gpio[1]  
    send packet with size = 3
@ send 4 pulses at gpio[2]  
    send packet with size = 4
@ send 4 pulses at gpio[3]  
    send packet with size = 5
@ send 4 pulses at gpio[4]  
    send packet with size = 6
@ send 4 pulses at gpio[5]  
    send packet with size = 7
@ send 4 pulses at gpio[6]  
    send packet with size = 8
@ send 4 pulses at gpio[7]  
    send packet with size = 9
@ send 4 pulses at gpio[8]  
    send packet with size = 10


@ reset pulses
    send packet with size = 1
@ send 4 pulses at gpio[9]  
    send packet with size = 2
@ send 4 pulses at gpio[10]  
    send packet with size = 3
@ send 4 pulses at gpio[11]  
    send packet with size = 4
@ send 4 pulses at gpio[12]  
    send packet with size = 5
@ send 4 pulses at gpio[13]  
    send packet with size = 6
@ send 4 pulses at gpio[14]  
    send packet with size = 7
@ send 4 pulses at gpio[15]  
    send packet with size = 8
@ send 4 pulses at gpio[16]  
    send packet with size = 9
@ send 4 pulses at gpio[17]  
    send packet with size = 10
@ send 4 pulses at gpio[18]  
    send packet with size = 11

@ test finish 
    send packet with size = 1
    send packet with size = 1
    send packet with size = 1


*/
void main()
{
	int i,j,high_chain_io;
    int num_pulses = 4;
    //int num_bits = 19;
    //configure_io0_37();

    reg_gpio_mode1 = 1;
    reg_gpio_mode0 = 0;
    reg_gpio_ien = 1;
    reg_gpio_oe = 1;
    int old_recieved;
    int recieved;

    set_registers();
    reg_mprj_datah = 0;
    reg_mprj_datal = 0;
    gpio_config_io();

    reg_gpio_out = 1; // OFF
    int flag = 0;
    int mask;
    int mask_io37 = 0x1 << 5;
    int io_num = 0;
    int recieved_bit;
    // send_packet_io0(2);

    while (1){
        flag = recieve_io37();
        // if (flag == 2){
        //     io_num = 0;
        //     flag = 1;
        //     // send_packet_io0(4);
        // }
        if (flag == 1){
            
            io_num++;
            mask = 0;
            high_chain_io = 37 - io_num;
            int counter = 0;
            // send_packet_io0(4);
            while(1){
                old_recieved = reg_mprj_datah & mask_io37;
                while(1){
                    recieved = reg_mprj_datah & mask_io37;
                    if (recieved != old_recieved){
                        // send_packet_io0(4);
                        recieved_bit = recieved >> 5;
                        if (high_chain_io<32){
                            mask = recieved_bit << io_num;
                            mask = mask | recieved_bit << high_chain_io;
                        }
                        else{
                            mask = recieved_bit << io_num;
                        }
                        if (high_chain_io>=32){
                            reg_mprj_datah = recieved_bit << high_chain_io-32;
                        }
                        reg_mprj_datal = mask;
                        // old_recieved = recieved;
                        // send_packet_io0(4);
                        counter++;
                        break;
                    }
                }
                if (counter == 4){
                    count_down(PULSE_WIDTH*2);
                    break;
                }
            }
        }
            
            // count_down(PULSE_WIDTH * 10); 
            // for (i = 0; i < num_pulses; i++){
            //     if (z>=32){
            //         reg_mprj_datah = 0x1 << z-32;
            //     }
            //     reg_mprj_datal = mask;
            //     count_down(PULSE_WIDTH); 
            //     reg_mprj_datah = 0x0;
            //     reg_mprj_datal = 0x0;  
            //     count_down(PULSE_WIDTH); 
            // }
        // }
    }

}

