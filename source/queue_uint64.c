
/**
 * @file queue_uint64.c
 * @brief Thread safe queue, which stores uint64_t
 * @details Call queue_init(queue_uint64_msg_t *q, int max_count) paired with queue_deinit(queue_uint64_msg_t *q) as their names imply, queue_initstruct(queue_uint64_msg_t *q)Initialize the message queue structure,*queue_get(queue_uint64_msg_t *q) and queue_put(queue_uint64_msg_t *q, void *data) In and out of the team operation
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2021/01/10
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/09 <td>1.0     <td>miaow     <td>Write this file
 * </table>
 */

#include <pthread.h>
#include <queue_uint64.h>
#ifdef QUEUE_UINT64_DEBUG
#include <stdio.h>
#include <stdint.h>
#endif
#include <stdlib.h>

/**
 * @brief Take out the first item from the circular queue
 * @param q The queue handler
 * @param data A buffer of uint64_t[1] to store the data taken out
 * @return 0 - success, -1 - failed
 */
int queue_uint64_get(queue_uint64_msg_t *q, uint64_t *data)
{
    pthread_mutex_lock(&q->_mux);
    // while (q->lget == q->lput && 0 == q->nData)
    // {
    //     // The reason program goes here: assuming there are 2 consmer threads block in this function
    //     // One wakes first and consumes 2 data quickly before another wakes
    //     // In the circumstances that the queue contains 2 items formerly, the second thread should not get data from an empty queue
    //     // This may happen when 2 queue_puts was called by producers and at that moment 2 consmer threads have been blocked

    //     // It is designed as a circular queue, where lget==lput means:
    //     // 1：nData!=0，a full queue
    //     // 2：nData为0，an empty queue
    //     q->nEmptyThread++;
    //     pthread_cond_wait(&q->_cond_get, &q->_mux);
    //     q->nEmptyThread--;
    // }
    if (q->nData == 0)
    {
        pthread_mutex_unlock(&q->_mux);
        return -1;
    }
#ifdef QUEUE_UINT64_DEBUG
    printf("get data! lget:%d, ", q->lget);
#endif
    *data = (q->buffer)[q->lget++];
#ifdef QUEUE_UINT64_DEBUG
    printf("data:% lld", *data);
#endif
    if (q->lget == q->size)
    {
        // this is a circular queue
        q->lget = 0;
    }
    q->nData--;
#ifdef QUEUE_UINT64_DEBUG
    printf(", nData:%d\r\n", q->nData);
#endif
    // if (q->nFullThread)
    // {
    //     // call pthread_cond_signal only when necessary, enter the kernel state as little as possible
    //     pthread_cond_signal(&q->_cond_put);
    // }
    pthread_mutex_unlock(&q->_mux);
    return 0;
}

/**
 * @brief Initialize the queue with a size (maximum count of items) specified in q->size
 * @param q The queue hander to be initialized
 * @return 0 - success, -1 - failed
 * @note q->size should be set before calling this function
 */
int queue_uint64_initstruct(queue_uint64_msg_t *q)
{
    q->buffer = malloc(q->size * sizeof(uint64_t));
    if (q->buffer == NULL)
        return -1;
    pthread_mutex_init(&q->_mux, NULL);
    // pthread_cond_init(&q->_cond_get, NULL);
    // pthread_cond_init(&q->_cond_put, NULL);
    return 0;
}

/**
 * @brief Initialize the queue
 * @param q The queue hander to be initialized
 * @param max_count Maximum count of items in the queue
 * @return 0 - success, -1 - failed
 */
int queue_uint64_init(queue_uint64_msg_t *q, int max_count)
{
    q->size = max_count;
    return queue_uint64_initstruct(q);
}

/**
 * @brief Deinitialize the queue
 * @param q The queue handle
 * @return 0 - success
 */
int queue_uint64_deinit(queue_uint64_msg_t *q)
{
    free(q->buffer);
    q->buffer = NULL;
    pthread_mutex_destroy(&q->_mux);
    // pthread_cond_destroy(&q->_cond_get);
    // pthread_cond_destroy(&q->_cond_put);
    q->size = 0;
    q->nData = 0;
    q->lget = 0;
    q->lput = 0;
    // q->nEmptyThread = 0;
    // q->nFullThread = 0;
    return 0;
}

/**
 * @brief Put one item into the circular queue
 * @param q The queue handle
 * @param data The item to put
 * @return 0 - success, -1 - failed
 */
int queue_uint64_put(queue_uint64_msg_t *q, uint64_t data)
{
    pthread_mutex_lock(&q->_mux);
    // while (q->lget == q->lput && q->nData)
    // {
    //     q->nFullThread++;
    //     pthread_cond_wait(&q->_cond_put, &q->_mux);
    //     q->nFullThread--;
    // }
    if (q->lget == q->lput && q->nData)
    {
        pthread_mutex_unlock(&q->_mux);
        return -1;
    }
#ifdef QUEUE_UINT64_DEBUG
    printf("put data! lput:%d, data:%lld", q->lput, data);
#endif
    (q->buffer)[q->lput++] = data;
    if (q->lput == q->size)
    {
        q->lput = 0;
    }
    q->nData++;
#ifdef QUEUE_UINT64_DEBUG
    printf(" nData:%d\n", q->nData);
#endif
    // if (q->nEmptyThread)
    // {
    //     pthread_cond_signal(&q->_cond_get);
    // }
    pthread_mutex_unlock(&q->_mux);
    return 0;
}

/**
 * @brief Clear the circular queue
 * @param q The queue handle
 * @return 0 - success, -1 - failed
 */
int queue_uint64_clear(queue_uint64_msg_t *q)
{
    pthread_mutex_lock(&q->_mux);
    // while (q->lget == q->lput && q->nData)
    // {
    //     q->nFullThread++;
    //     pthread_cond_wait(&q->_cond_put, &q->_mux);
    //     q->nFullThread--;
    // }
    q->lget = q->lput = q->nData = 0;
#ifdef QUEUE_UINT64_DEBUG
    printf("clear!\r\n");
#endif

    // if (q->nEmptyThread)
    // {
    //     pthread_cond_signal(&q->_cond_get);
    // }
    pthread_mutex_unlock(&q->_mux);
    return 0;
}