/**
 * @file encoder_dev.h
 * @brief Manage the hardware encoder unit
 * @author miaow, lzy (3703781@qq.com)
 * @version 0.11
 * @date 2022/04/26
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2023  miaow, lyz
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/11 <td>0.9     <td>Miaow    <td>Write this module
 * <tr><td>2022/04/11 <td>0.10    <td>lyz      <td>Add seprate dividers up to 4 cameras
 * <tr><td>2023/04/26 <td>0.11    <td>Miaow    <td>Add Clear mode
 * </table>
 */
#ifndef __ENCODER_DEV_H
#define __ENCODER_DEV_H

#include <stdint.h>

#define ENCODER_DEV_PATH "/dev/encoder"

#define ENCODER_DEV_DIVIDE_NOT_TO_SET 0

typedef enum
{
    ENCODER_TRIG_MODE_EXTERNEL = 100,
    ENCODER_TRIG_MODE_INTERNEL = 101
} encoder_dev_trig_mode_enum;

typedef enum
{
    ENCODER_CLEAR_MODE_BOTH = 200,
    ENCODER_CLEAR_MODE_INTERNAL = 201
} encoder_dev_clear_mode_enum;

int encoder_dev_set_divide(int camera_a_divide,
                           int camera_b_divide,
                           int camera_c_divide,
                           int camera_d_divide);
int encoder_dev_flush(void);
int encoder_dev_set_trigmod(encoder_dev_trig_mode_enum mode);
int encoder_dev_set_clrmod(encoder_dev_clear_mode_enum mode);
int encoder_dev_virtual_trig(int count);
int encoder_dev_init(void);
int encoder_dev_deinit(void);

#endif
