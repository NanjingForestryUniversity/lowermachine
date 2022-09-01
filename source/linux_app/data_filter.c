/**
 * @file data_filter.c
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

#include <stdlib.h>
#include <string.h>
#include <data_filter.h>

void datafilter_init(datafilter_typedef *filter, int w_size)
{
    filter->cache = (int *)malloc(sizeof(int) * (w_size + 1));
    memset(filter->cache, 0, sizeof(int) * (w_size + 1));

    filter->w_size = w_size;
    filter->sum = 0;
    filter->head = 0;
}

int datafilter_calculate(datafilter_typedef *filter, int z)
{
    filter->cache[filter->head] = z;
    filter->head = (filter->head + 1) % (filter->w_size + 1);
    filter->sum = filter->sum + z - filter->cache[filter->head];
    if (filter->w_size != 0)
        return filter->sum / filter->w_size;
    else
        return -1;
}

void datafilter_deinit(datafilter_typedef *filter)
{
    if (filter->cache != NULL)
    {
        free(filter->cache);
        filter->cache = NULL;
    }
    filter->sum = 0;
    filter->w_size = 0;
    filter->head = 0;
}
