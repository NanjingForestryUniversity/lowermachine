/**
 * @file common.h
 * @brief Common macros.
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/06/12
 * @mainpage github.com/NanjingForestryUniversity
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/12 <td>1.0     <td>miaow     <td>Write this file
 * </table>
 */
#ifndef __COMMON_H
#define __COMMON_H

#include <stdio.h>
#include <errno.h>

#define ON_ERROR(res, message1, message2)                                                                 \
    if (res < 0)                                                                                          \
    {                                                                                                     \
        sprintf(perror_buffer, "error %d at %s:%d, %s, %s", res, __FILE__, __LINE__, message1, message2); \
        perror(perror_buffer);                                                                            \
    }

#define ON_ERROR_RET_VOID(res, message1, message2) \
    ON_ERROR(res, message1, message2);             \
    if (res < 0)                                   \
    {                                              \
        res = 0;                                   \
        return;                                    \
    }

#define ON_ERROR_RET(res, message1, message2, retval) \
    ON_ERROR(res, message1, message2);                \
    if (res < 0)                                      \
    {                                                 \
        res = 0;                                      \
        return retval;                                \
    }
    
#endif