#define  PULSE_WIDTH   250000

void count_down(const int d)
{
    /* Configure timer for a single-shot countdown */
    reg_timer0_config = 0;
    reg_timer0_data = d;
    reg_timer0_config = 1; /* Enabled, one-shot, down count */

    // Loop, waiting for value to reach zero
    reg_timer0_update = 1;  // latch current value
    while (reg_timer0_value > 0) {
        reg_timer0_update = 1;
    }
}


void send_pulse_io0(){
    int mask = 0xFFFFFFFE;
    int temp = reg_mprj_datal&mask;
    reg_mprj_datal = temp; // 0
    count_down(PULSE_WIDTH);
    temp = reg_mprj_datal;
    reg_mprj_datal = temp | 1; // 1
    count_down(PULSE_WIDTH);  
}

void send_pulse_io37(){
    int mask = 0x1F;
    int temp = reg_mprj_datah&mask;
    reg_mprj_datah = temp; // 0
    count_down(PULSE_WIDTH);
    temp = reg_mprj_datah;
    reg_mprj_datal = temp | 1; // 1
    count_down(PULSE_WIDTH);  
}


void send_packet_io0(int num_pulses){
    // send pulses
    for (int i = 0; i < num_pulses+1; i++){
        send_pulse_io0();
    }
    // end of packet
    count_down(PULSE_WIDTH*10);
}

void send_packet_io37(int num_pulses){
    // send pulses
    for (int i = 0; i < num_pulses+1; i++){
        send_pulse_io37();
    }
    // end of packet
    count_down(PULSE_WIDTH*10);
}


void configure_io0_37(){
    reg_mprj_xfer = 0x66; reg_mprj_xfer = 0x76; // 11
reg_mprj_xfer = 0x06; reg_mprj_xfer = 0x16;

    for (int count = 0; count < 7; count++) {
	   reg_mprj_xfer = 0x06; reg_mprj_xfer = 0x16; // 00
    }

    reg_mprj_xfer = 0x66; reg_mprj_xfer = 0x76; // 11
    reg_mprj_xfer = 0x06; reg_mprj_xfer = 0x16; // 00
    reg_mprj_xfer = 0x06; reg_mprj_xfer = 0x16; // 00
    reg_mprj_xfer = 0x66; reg_mprj_xfer = 0x76; // 11
    // load
    reg_mprj_xfer = 0x06;
    reg_mprj_xfer = 0x0e; 
    reg_mprj_xfer = 0x06;		// Apply load
}

