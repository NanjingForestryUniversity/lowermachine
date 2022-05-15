#include "fifo.h"

#define FIFO_U64_TO_REG_1(a, b) ((u32)(a))
#define FIFO_U64_TO_REG_2(a, b) (((u32)(a >> 32)) | ((u32)b << 16))
#define FIFO_U64_TO_REG_3(a, b) ((u32)(a >> 16))

#define FIFO_ARRAY_TO_REG(a, idx) (a[idx] | (u32)a[idx+1] << 8 | (u32)a[idx+2] << 16 | (u32)a[idx+3] << 24)

ip_fifo_typedef *ip_fifo_inst = ((ip_fifo_typedef *)IP_FIFO_BASE);

void fifo_putb(u8 const * block, u32 count)
{
	u32 line_count = count / 36;
	u8 * tmp_block_ptr = block;
	ip_fifo_inst->reg9 = 0;
	ip_fifo_inst->reg10 = 0;
	ip_fifo_inst->reg11 = 0;
	while (line_count--)
	{
		ip_fifo_inst->reg0 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 0);
		ip_fifo_inst->reg1 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 4);
		ip_fifo_inst->reg2 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 8);
		ip_fifo_inst->reg3 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 12);
		ip_fifo_inst->reg4 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 16);
		ip_fifo_inst->reg5 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 20);
		ip_fifo_inst->reg6 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 24);
		ip_fifo_inst->reg7 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 28);
		ip_fifo_inst->reg8 = FIFO_ARRAY_TO_REG(tmp_block_ptr, 32);
		ip_fifo_inst->reg14 = 1;
		tmp_block_ptr += 36;
	}

}

void fifo_puta(u8 const * line)
{
	ip_fifo_inst->reg0 = FIFO_ARRAY_TO_REG(line, 0);
	ip_fifo_inst->reg1 = FIFO_ARRAY_TO_REG(line, 4);
	ip_fifo_inst->reg2 = FIFO_ARRAY_TO_REG(line, 8);
	ip_fifo_inst->reg3 = FIFO_ARRAY_TO_REG(line, 12);
	ip_fifo_inst->reg4 = FIFO_ARRAY_TO_REG(line, 16);
	ip_fifo_inst->reg5 = FIFO_ARRAY_TO_REG(line, 20);
	ip_fifo_inst->reg6 = FIFO_ARRAY_TO_REG(line, 24);
	ip_fifo_inst->reg7 = FIFO_ARRAY_TO_REG(line, 28);
	ip_fifo_inst->reg8 = FIFO_ARRAY_TO_REG(line, 32);

	ip_fifo_inst->reg9 = 0;
	ip_fifo_inst->reg10 = 0;
	ip_fifo_inst->reg11 = 0;

	ip_fifo_inst->reg14 = 1;
}

void fifo_puts(valveboard_data_typedef* valveboard_data_sturcture)
{
	ip_fifo_inst->reg0 = FIFO_U64_TO_REG_1(valveboard_data_sturcture->valveboard1, 0UL);
	ip_fifo_inst->reg1 = FIFO_U64_TO_REG_2(valveboard_data_sturcture->valveboard1, valveboard_data_sturcture->valveboard2);
	ip_fifo_inst->reg2 = FIFO_U64_TO_REG_3(valveboard_data_sturcture->valveboard2, 0UL);

	ip_fifo_inst->reg3 = FIFO_U64_TO_REG_1(valveboard_data_sturcture->valveboard3, 0UL);
	ip_fifo_inst->reg4 = FIFO_U64_TO_REG_2(valveboard_data_sturcture->valveboard3, valveboard_data_sturcture->valveboard4);
	ip_fifo_inst->reg5 = FIFO_U64_TO_REG_3(valveboard_data_sturcture->valveboard4, 0UL);

	ip_fifo_inst->reg6 = FIFO_U64_TO_REG_1(valveboard_data_sturcture->valveboard5, 0UL);
	ip_fifo_inst->reg7 = FIFO_U64_TO_REG_2(valveboard_data_sturcture->valveboard5, valveboard_data_sturcture->valveboard6);
	ip_fifo_inst->reg8 = FIFO_U64_TO_REG_3(valveboard_data_sturcture->valveboard6, 0UL);

	ip_fifo_inst->reg9 = 0;
	ip_fifo_inst->reg10 = 0;
	ip_fifo_inst->reg11 = 0;

	ip_fifo_inst->reg14 = 1;
}

u32 fifo_get_count()
{
	return ip_fifo_inst->reg12 & 0xFFF;
}
