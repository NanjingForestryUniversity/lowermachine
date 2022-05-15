#include "encoder.h"

ip_encoder_typedef *ip_encoder_inst = ((ip_encoder_typedef *)IP_ENCODER_BASE);

void encoder_init(u32 valve_divider, u32 camera_divider)
{
	ip_encoder_inst->reg0 &= ~(u32)(1<<0);
	ip_encoder_inst->reg1 = valve_divider;
	ip_encoder_inst->reg2 = camera_divider;
	ip_encoder_inst->reg0 |= (u32)(1<<0);
}

void encoder_set_valve_divider(u32 divider)
{
	ip_encoder_inst->reg0 &= ~(u32)(1<<0);
	ip_encoder_inst->reg1 = divider;
}

void encoder_set_camera_divider(u32 divider)
{
	ip_encoder_inst->reg0 &= ~(u32)(1<<0);
	ip_encoder_inst->reg2 = divider;
}

void encoder_start()
{
	ip_encoder_inst->reg0 |= (u32)(1<<0);
}

void encoder_stop()
{
	ip_encoder_inst->reg0 &= ~(u32)(1<<0);
}
