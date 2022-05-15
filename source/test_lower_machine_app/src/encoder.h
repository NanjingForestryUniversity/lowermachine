#ifndef __ENCODER_H
#define __ENCODER_H

#include "xil_types.h"

#define IP_ENCODER_BASE 0x43C10000

typedef struct{
	volatile u32 reg0;
	volatile u32 reg1;
	volatile u32 reg2;
	volatile u32 reg3;
}ip_encoder_typedef;


extern ip_encoder_typedef *ip_encoder_inst;

void encoder_init(u32 valve_divider, u32 camera_divider);
void encoder_set_valve_divider(u32 divider);
void encoder_set_camera_divider(u32 divider);
void encoder_start(void);
void encoder_stop(void);

#endif
