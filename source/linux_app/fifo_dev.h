/**
 * @file fifo_dev.h
 * @brief Operate the hardware fifo with Linux application
 * @details Call fifo_dev_init() paired with fifo_dev_deinit() as their names imply, fifo_dev_write_xxx() can be executed several times to operate the hardware fifo between fifo_dev_init() and fifo_dev_deinit()
 * @mainpage github.com/NanjingForestryUniversity
 * @author miaow (3703781@qq.com)
 * @version 1.1
 * @date 2022/08/07
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2022  miaow
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/09 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2022/08/07 <td>1.1     <td>miaow     <td>Add ignore_row_num to fifo_dev_write_frame
 * </table>
 */
#ifndef __FIFO_DEV_H
#define __FIFO_DEV_H

#include <stdint.h>

#define FIFO_DEV_PATH "/dev/fifo"

int fifo_dev_init(void);
int fifo_dev_get_emptycount(void);
int fifo_dev_write_frame(void *valve_data, int ignore_row_num);
int fifo_dev_clear(void);
int fifo_dev_write_delay(uint32_t count);
int fifo_dev_write_row(void *valve_data);
int fifo_dev_get_count(void);

int fifo_dev_deinit(void);

#endif