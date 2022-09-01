/**
 * @file host_computer.h
 * @brief Commnunicate with host computer. Protocal is described in hostcomputer通信协议.md
 * @author miaow (3703781@qq.com)
 * @version 1.1
 * @date 2022/08/6
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/16 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2022/08/06 <td>1.1     <td>miaow     <td>Add fifob
 * </table>
 */
#ifndef __HOST_COMPUTER_H
#define __HOST_COMPUTER_H

#include <queue_uint64.h>
#include <pthread.h>
#include <stdint.h>

#define HOST_COMPUTER_IP "192.168.10.8"
#define HOST_COMPUTER_PORT 13452
#define HOST_COMPUTER_PICTURE_ROW_NUM 1024
#define HOST_COMPUTER_PICTURE_COLUMN_NUM 256
#define HOST_COMPUTER_PICTURE_COLUMN_BYTES (HOST_COMPUTER_PICTURE_COLUMN_NUM / 8)
#define HOST_COMPUTER_PICTURE_BYTES (HOST_COMPUTER_PICTURE_COLUMN_BYTES * HOST_COMPUTER_PICTURE_ROW_NUM)
#define HOST_COMPUTER_PICTURES_BEGINNING_IGNORE_NUM 1

/**
 * @brief The commonds, ref 通信协议
 */
enum HOSTCOMPUTER_CMD
{
    HOSTCOMPUTER_CMD_START = 2,
    HOSTCOMPUTER_CMD_STOP = 3,
    HOSTCOMPUTER_CMD_TEST = 4,
    HOSTCOMPUTER_CMD_POWERON = 5,
    HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT = 6,
    HOSTCOMPUTER_CMD_SETVALVETRIGPULSECOUNT = 7,
    HOSTCOMPUTER_CMD_SETCAMERATOVALVEPULSECOUNT = 8,
    HOSTCOMPUTER_CMD_STOP_TEST = 9
};

int hostcomputer_init(queue_uint64_msg_t *cmd_q);
int hostcomputer_deinit(void);

#endif
