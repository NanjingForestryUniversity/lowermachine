/**
 * @file camera_trigger.c
 * @brief Control the camera to grab frames
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/01/09
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/09 <td>1.0     <td>miaow     <td>Write this file
 * </table>
 */
#ifndef __CAMERA_TRIGGER_H
#define __CAMERA_TRIGGER_H
#include <gpio_common.h>

typedef enum
{
    TRIG_LINE=GPIO_PINDEF_TO_INDEX(GPO6)
}cameratrigger_pin_enum_t;

int cameratrigger_init(void);
int cameratrigger_trig(void);
int cameratrigger_deinit(void);

#endif