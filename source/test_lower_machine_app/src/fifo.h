#ifndef __FIFO_H
#define __FIFO_H

#include "xil_types.h"

#define IP_FIFO_BASE 0x43C00000


typedef struct{
	volatile u32 reg0;
	volatile u32 reg1;
	volatile u32 reg2;
	volatile u32 reg3;
	volatile u32 reg4;
	volatile u32 reg5;
	volatile u32 reg6;
	volatile u32 reg7;
	volatile u32 reg8;
	volatile u32 reg9;
	volatile u32 reg10;
	volatile u32 reg11;
	volatile u32 reg12;  // {16'b0, almost_empty, empty, almost_full, full, data_count[11:0]};
	volatile u32 reg13;
	volatile u32 reg14;
}ip_fifo_typedef;

typedef struct{
	u64 valveboard1;
	u64 valveboard2;
	u64 valveboard3;
	u64 valveboard4;
	u64 valveboard5;
	u64 valveboard6;
}valveboard_data_typedef;

extern ip_fifo_typedef *ip_fifo_inst;

void fifo_put(valveboard_data_typedef valveboard_data_sturcture);
void fifo_putb(u8 const * block, u32 count);
void fifo_puta(u8 const * line);
void fifo_puts(valveboard_data_typedef* valveboard_data_sturcture);
u32 fifo_get_count();

#endif  // __FIFO_H
