/**
 * @file encoder.c
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
#include <poll.h>
#include <stdlib.h>
#include <encoder.h>
#include <pthread.h>
#include <stdint.h>
#include <gpio_common.h>


#define __GPI_GET(pin_t) read(gpi_value_fd[GPIO_PINDEF_TO_INDEX(pin_t)], _global_structure.buf, sizeof(_global_structure.buf))

/**
 * @brief Variables definition used in this module
 */
typedef struct
{
    int need_exit;  // loop_thread joins to parent-thread at need_exit==1
    pthread_t loop_thread;  // The main deamon thread
    encoder_callback callback_func;  // Restore the pointer to callback function
    pthread_mutex_t loop_thread_mutex;  // Used in the main deamon thread and deinit function, surrounding the need_exit variable
    char buf[1];  // Buffer for reading the file descripter
} encoder_global_t;


static encoder_global_t _global_structure;  //! the global variables used in this file (module)

static void *loop_thread_func(void *param);

/**
 * @brief Initialize the encoder related gpio and thread 
 * @param func The callback function, which is called at rising edge of the encoder
 * @return 0-success, -1 - failed
 */
int encoder_init(encoder_callback func)
{

    int phase_b_index = GPIO_PINDEF_TO_INDEX(ENCODER_PHASEB);
    // export
    int fd_export = open(GPIO_EXPORT_PATH, O_WRONLY);
    ON_ERROR_RET(fd_export, GPIO_EXPORT_PATH, "export in encoder_init()", -1);

    if (!is_file_exist(gpio_value_file_gpi_list[phase_b_index]))  // do not export if value file exist
    {
        int ret = write(fd_export, gpi_pin_str[phase_b_index], gpi_pin_str_len[phase_b_index]);
        ON_ERROR_RET(ret, gpi_pin_str[phase_b_index], "open value file in encoder_init()", -1);
    }
    close(fd_export);

    // open edge file
    int edge_fd = open(gpio_edge_file_gpi_list[phase_b_index], O_RDWR);
    ON_ERROR_RET(edge_fd, gpio_edge_file_gpi_list[phase_b_index], "open edge file in encoder_init()", -1);
    write(edge_fd, "rising", 7);
    close(edge_fd);

    // open value file
    gpi_value_fd[phase_b_index] = open(gpio_value_file_gpi_list[phase_b_index], O_RDWR);
    ON_ERROR_RET(gpi_value_fd[phase_b_index], gpio_value_file_gpi_list[phase_b_index], "open value file in encoder_init()", -1);

    _global_structure.callback_func = func;

    // start loop thread
    pthread_create(&_global_structure.loop_thread, NULL, loop_thread_func, NULL);

    return 0;
}

/**
 * @brief Deinitialize the encoder module, stop the thread and release resources
 * @return 0-success, -1 - failed
 */
int encoder_deinit()
{
    // stop loop_thread
    pthread_mutex_lock(&_global_structure.loop_thread_mutex);
    _global_structure.need_exit = 1;
    pthread_mutex_unlock(&_global_structure.loop_thread_mutex);
    // wait loop_thread to stop
    pthread_join(_global_structure.loop_thread, NULL);
    pthread_mutex_destroy(&_global_structure.loop_thread_mutex);
    _global_structure.need_exit = 0;
    // close value file
    int ret = close(gpi_value_fd[GPIO_PINDEF_TO_INDEX(ENCODER_PHASEB)]);
    ON_ERROR_RET(ret, "close value file in encoder_init()", "", -1);
    gpi_value_fd[GPIO_PINDEF_TO_INDEX(ENCODER_PHASEB)] = 0;
    return 0;
}

/**
 * @brief Call the callback function set when initialization at rising edge of the encoder pulse
 * @param param Not used
 * @return 0
 */
static void *loop_thread_func(void *param)
{
    // 调用一次encoder_callback func
    printf("loop thread in %s start\r\n", __FILE__);
    struct pollfd fds[1];
    fds[0].fd = gpi_value_fd[GPIO_PINDEF_TO_INDEX(ENCODER_PHASEB)];
    fds[0].events = POLLPRI;
    int need_exit = 0;
    
    while (!need_exit)
    {
        if (poll(fds, 1, 1000) && (fds[0].revents & POLLPRI))
        {
            __GPI_GET(ENCODER_PHASEB);
            _global_structure.callback_func();
        }
        pthread_mutex_lock(&_global_structure.loop_thread_mutex);
        need_exit = _global_structure.need_exit;
        pthread_mutex_unlock(&_global_structure.loop_thread_mutex);
    }
    printf("loop thread in %s exit\r\n", __FILE__);
    return (void *)NULL;
}

