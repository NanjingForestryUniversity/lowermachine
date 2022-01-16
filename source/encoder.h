/**
 * @file encoder.h
 * @brief Manage the encoder and realize a callback function
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/01/09
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/09 <td>1.0     <td>Miaow     <td>Write this module
 * </table>
 */
#ifndef __ENCODER_H
#define __ENCODER_H
#include <gpio_common.h>

/**
 * @brief Pin definition
 * @note Actually, only ENCODER_PHASEB is used
 */
typedef enum
{
    ENCODER_PHASEA=GPIO_PINDEF_TO_INDEX(GPI0),
    ENCODER_PHASEB=GPIO_PINDEF_TO_INDEX(GPI2)
}encoder_pin_enum_t;

typedef void (*encoder_callback)(void);  // Callback funtion prototype.

int encoder_init(encoder_callback func);
int encoder_deinit(void);

#endif
