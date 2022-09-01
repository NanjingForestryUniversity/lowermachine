/**
 * @file data_filter.h
 * @brief Manage the hardware encoder unit
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/08/06
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/08/06 <td>1.0     <td>Miaow     <td>Write this module
 * </table>
 */
#ifndef __DATA_FILTER_H
#define __DATA_FILTER_H

typedef struct
{
    int w_size;
    int head;
    int sum;
    int *cache;
} datafilter_typedef;

void datafilter_init(datafilter_typedef *filter, int w_size);

int datafilter_calculate(datafilter_typedef *filter, int z);

void datafilter_deinit(datafilter_typedef *filter);


#endif
