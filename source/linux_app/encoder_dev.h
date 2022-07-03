/**
 * @file encoder_dev.h
 * @brief Manage the hardware encoder unit
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/06/11
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/11 <td>0.9     <td>Miaow     <td>Write this module
 * </table>
 */
#ifndef __ENCODER_DEV_H
#define __ENCODER_DEV_H

#include <stdint.h>

#define ENCODER_DEV_PATH "/dev/encoder"

#define ENCODER_DEV_DIVIDE_NOT_TO_SET   0

#define ENCODER_TRIG_MODE_EXTERNEL 100
#define ENCODER_TRIG_MODE_INTERNEL 101

int encoder_dev_set_divide(int valve_divide, int camera_divide);
int encoder_dev_flush(void);
int encoder_dev_set_trigmod(int mode);
int encoder_dev_virtual_trig(int count);
int encoder_dev_init(void);
int encoder_dev_deinit(void);

#endif
