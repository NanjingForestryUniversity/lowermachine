/**
 * @file queue_reference.h
 * @brief Thread safe queue, which stores void pointers
 * @details Call queue_init(queue_reference_msg_t *q, int max_count) paired with queue_deinit(queue_reference_msg_t *q) as their names imply, queue_initstruct(queue_reference_msg_t *q)Initialize the message queue structure,*queue_get(queue_reference_msg_t *q) and queue_put(queue_reference_msg_t *q, void *data) In and out of the team operation
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2021/12/25 merry christmas
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/09 <td>1.0     <td>miaow     <td>Write this file
 * </table>
 */
#if !defined(__QUEUE_REFERENCE_H)
#define __QUEUE_REFERENCE_H

#include <pthread.h>

/**
 * @brief Queue handle structure
 */
typedef struct
{
    void **buffer;    // 缓冲数据, .buffer = msg
    int size;         // 队列大小，使用的时候给出稍大的size，可以减少进入内核态的操作
    int lget;         // 取队列数据的偏移量
    int lput;         // 放队列数据的偏移量
    int nData;        // 队列中数据的个数,用来判断队列满/空
    // int nFullThread;  // 由于队列满而阻塞在put_queue的线程个数
    // int nEmptyThread; // 由于队列空而阻塞在get_queue的线程个数
    pthread_mutex_t _mux;
    // pthread_cond_t _cond_get, _cond_put;
} queue_reference_msg_t;

// #define QUEUE_REFERENCE_DEBUG

void *queue_reference_get(queue_reference_msg_t *q);
int queue_reference_put(queue_reference_msg_t *q, void *data);
int queue_reference_initstruct(queue_reference_msg_t *q);
int queue_reference_init(queue_reference_msg_t *q, int max_count);
int queue_reference_deinit(queue_reference_msg_t *q);

#endif // __QUEUE_REFERENCE_H
