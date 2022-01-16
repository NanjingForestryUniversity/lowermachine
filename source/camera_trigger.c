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
#include <camera_trigger.h>
#include <gpio_common.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>
#include <time.h>

// Write to the file desc (global variable `gpo_value_fd` in gpio_common.c) to operate a gpio.
// So gpo_value_fd should be initialized in valve_init with great care.
// Also, gpo_value_fd/gpi_value_fd is used in other .c files (read pluse of encoder, etc).
#define __GPO_SET_BIT(pin_t) __GPO_SET(pin_t, GPIO_VALUE_HIGH)
#define __GPO_CLR_BIT(pin_t) __GPO_SET(pin_t, GPIO_VALUE_LOW)
#define __GPO_SET(pin_t, value_t) write(gpo_value_fd[GPIO_PINDEF_TO_INDEX(pin_t)], gpio_pin_value_str[GPIO_VALUEDEF_TO_INDEX(value_t)], gpio_pin_value_str_len[GPIO_VALUEDEF_TO_INDEX(value_t)])

/**
 * @brief Variables definition used in this module
 */
typedef struct
{
    sem_t need_send;  // Value >= 0 will cause a the camera grabbing one frame
    sem_t is_sending; // value >= 0 means the last trigger signal is sent
    pthread_mutex_t loop_thread_mutex;
    int need_exit;         // loop_thread joins to parent-thread at need_exit==1
    pthread_t loop_thread; // The sending thread
} cameratrigger_global_t;

static cameratrigger_global_t _global_structure;

static void *loop_thread_func(void *param);

/**
 * @brief Initialize camera trigger gpo and start loop_thread which keeps listening the trig signal
 * @return 0 - success, -1 - error
 */
int cameratrigger_init()
{
    int trig_line_index = GPIO_PINDEF_TO_INDEX(TRIG_LINE);
    // export the trigger line
    int fd_export = open(GPIO_EXPORT_PATH, O_WRONLY);
    ON_ERROR_RET(fd_export, GPIO_EXPORT_PATH, "export in cameratrigger_init()", -1);

    if (!is_file_exist(gpio_value_file_gpo_list[trig_line_index]))
    {
        int ret = write(fd_export, gpo_pin_str[trig_line_index], gpo_pin_str_len[trig_line_index]);
        ON_ERROR_RET(ret, gpo_pin_str[trig_line_index], "open value file in cameratrigger_init()", -1);
    }
    close(fd_export);

    gpo_value_fd[trig_line_index] = open(gpio_value_file_gpo_list[trig_line_index], O_RDWR);
    ON_ERROR_RET(gpo_value_fd[trig_line_index], gpio_value_file_gpo_list[trig_line_index], "open value file in cameratrigger_init()", -1);
    __GPO_SET_BIT(TRIG_LINE);

    sem_init(&_global_structure.need_send, 0, 0);
    sem_init(&_global_structure.is_sending, 0, 1);
    pthread_mutex_init(&_global_structure.loop_thread_mutex, NULL);

    int ret = pthread_create(&_global_structure.loop_thread, NULL, loop_thread_func, NULL);
    ON_ERROR_RET(ret, "thread create error in cameratrigger_init()", "", -1);

    return 0;
}

/**
 * @brief This function runs in child thread and triggles the camera to grab one frame
 */
void *loop_thread_func(void *param)
{
    printf("loop_thread in %s start\r\n", __FILE__);
    int need_exit = 0;
    struct timespec ts;
    int ret = 0;
    while (!need_exit)
    {

        clock_gettime(CLOCK_REALTIME, &ts);
        ts.tv_sec += 1;
        ret = sem_timedwait(&_global_structure.need_send, &ts);
        if (ret == 0)
        {
            __GPO_CLR_BIT(TRIG_LINE);
            usleep(200);
            __GPO_SET_BIT(TRIG_LINE);
            sem_post(&_global_structure.is_sending);
        }
        pthread_mutex_lock(&_global_structure.loop_thread_mutex);
        need_exit = _global_structure.need_exit;
        pthread_mutex_unlock(&_global_structure.loop_thread_mutex);
    }
    printf("loop_thread in %s exit\r\n", __FILE__);
    return NULL;
}

/**
 * @brief Trigger a frame grabbing of the camera
 * @note This function will wait until last grabbing accomplished
 * @return 0 - success
 */
int cameratrigger_trig()
{
    sem_wait(&_global_structure.is_sending);
    sem_post(&_global_structure.need_send);
    return 0;
}

/**
 * @brief Deinitialize and release all resources of this module
 * @note This function DOES BLOCKS 1s at most and DOES NOT UNEXPORT gpo
 * @return 0 - success, -1 - error
 */
int cameratrigger_deinit()
{
    sem_wait(&_global_structure.is_sending);
    pthread_mutex_lock(&_global_structure.loop_thread_mutex);
    _global_structure.need_exit = 1;
    pthread_mutex_unlock(&_global_structure.loop_thread_mutex);
    pthread_join(_global_structure.loop_thread, NULL);
    pthread_mutex_destroy(&_global_structure.loop_thread_mutex);
    sem_destroy(&_global_structure.is_sending);
    sem_destroy(&_global_structure.need_send);
    _global_structure.need_exit = 0;

    int ret = close(gpo_value_fd[GPIO_PINDEF_TO_INDEX(TRIG_LINE)]);
    ON_ERROR_RET(ret, "close value file in cameratrigger_deinit()", "", -1);

    return 0;
}