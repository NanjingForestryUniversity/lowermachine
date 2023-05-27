/**
 * @file host_computer.h
 * @brief Commnunicate with host computer. Protocal is described in 下位机和上位机通信协议 V1.4
 * @author miaow (3703781@qq.com)
 * @version 1.2
 * @date 2023/05/07
 * @mainpage github.com/NanjingForestryUniversity
 * 
 * @copyright Copyright (c) 2023  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/16 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2022/08/06 <td>1.1     <td>miaow     <td>Add fifob
 * <tr><td>2023/05/07 <td>1.2     <td>miaow     <td>Port to b03 branch 
 * </table>
 */
#ifndef __HOST_COMPUTER_H
#define __HOST_COMPUTER_H

#include <queue_uint64.h>
#include <pthread.h>
#include <stdint.h>

#define HOST_COMPUTER_IP "192.168.2.125"
#define HOST_COMPUTER_PORT 13452

/**
 * @brief The commonds, ref 下位机和上位机通信协议V1.4
 */
enum HOSTCOMPUTER_CMD
{
    HOSTCOMPUTER_CMD_START = 1,
    HOSTCOMPUTER_CMD_STOP = 2,
    HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_A = 3,
    HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_B = 4,
    HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_C = 5,
    HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_D = 6,
};

int hostcomputer_init(queue_uint64_msg_t *cmd_q);
int hostcomputer_deinit(void);

#endif
