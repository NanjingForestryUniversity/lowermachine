/**
 * @file host_computer.h
 * @brief Commnunicate with host computer. Protocal is described in 下位机和上位机通信协议.md
 * @author miaow (3703781@qq.com)
 * @version 1.1
 * @date 2023/02/08
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/16 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2023/02/08 <td>1.1     <td>miaow     <td>Add 3 macros for picture from host computer
 * </table>
 */
#ifndef __HOST_COMPUTER_H
#define __HOST_COMPUTER_H

#include <queue_uint64.h>
#include <pthread.h>
#include <stdint.h>

#define HOST_COMPUTER_IP "192.168.2.10"
#define HOST_COMPUTER_PORT 13452
#define HOST_COMPUTER_PICTURE_ROW_NUM 500
#define HOST_COMPUTER_PICTURE_COLUMN_NUM 48
#define HOST_COMPUTER_PICTURE_COLUMN_BYTES (HOST_COMPUTER_PICTURE_COLUMN_NUM / 8)
#define HOST_COMPUTER_PICTURE_BYTES (HOST_COMPUTER_PICTURE_COLUMN_BYTES * HOST_COMPUTER_PICTURE_ROW_NUM)

/**
 * @brief The commonds, ref hostcomputer通信协议.md
 */
enum HOSTCOMPUTER_CMD
{
    HOSTCOMPUTER_CMD_START = 2,
    HOSTCOMPUTER_CMD_STOP = 3,
    HOSTCOMPUTER_CMD_TEST = 4,
    HOSTCOMPUTER_CMD_POWERON = 5,
    HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT = 6,
    HOSTCOMPUTER_CMD_SETVALVETRIGPULSECOUNT = 7,
    HOSTCOMPUTER_CMD_SETCAMERATOVALVEPULSECOUNT = 8
    
};

int hostcomputer_init(queue_uint64_msg_t *data_q, queue_uint64_msg_t *cmd_q);
int hostcomputer_deinit(void);

#endif
