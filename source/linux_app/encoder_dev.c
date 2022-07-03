/**
 * @file encoder_dev.c
 * @brief Manage the hardware encoder unit
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/06/11
 * @mainpage github.com/NanjingForestryUniversity
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/11 <td>0.9     <td>Miaow     <td>Write this module
 * </table>
 */

#include <stdlib.h>
#include <encoder_dev.h>
#include <stdint.h>
#include <common.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>

#define ENCODER_CMD_FUNCTION_CLEAR 1
#define ENCODER_CMD_FUNCTION_VIRT_INPUT 2

static int encoder_dev_fd = -1;
static char perror_buffer[128];

static struct {
        unsigned int valve_divide_value;
        unsigned int camera_divide_value;
} encoder_dev_divide_value_structure;

/**
 * @brief Initialize the hardware encoder unit
 * @note This function just open the file descriptor of the hardware encoder unit
 * @return 0 - success, other - error
 */
int encoder_dev_init()
{
    encoder_dev_fd = open(ENCODER_DEV_PATH, O_RDWR);
    ON_ERROR_RET(encoder_dev_fd, "", "", -1);
    return 0;
}

/**
 * @brief Set the two divider in the hareware encoder unit.
 * @param valve_divide the frequency division factor between the encoder signal and valve output
 *                      Set ENCODER_DEV_DIVIDE_NOT_TO_SET to skip changing the division facter
 * @param camera_divide the frequency division factor between the encoder signal and camera triggle signal
 *                      Set ENCODER_DEV_DIVIDE_NOT_TO_SET to skip changing the division facter
 *  
 * @return 0 - success, other - error
 */
int encoder_dev_set_divide(int valve_divide, int camera_divide)
{
    encoder_dev_divide_value_structure.valve_divide_value = valve_divide;
    encoder_dev_divide_value_structure.camera_divide_value = camera_divide;
    ssize_t size = write(encoder_dev_fd, &encoder_dev_divide_value_structure, sizeof(encoder_dev_divide_value_structure));
    int res = -(size != sizeof(encoder_dev_divide_value_structure));
    ON_ERROR_RET(res, "size=", "", -1);

    return 0;
}

/**
 * @brief Set the trig signal to internal or external.
 * @param mode ENCODER_TRIG_MODE_EXTERNEL for externally trig, or ENCODER_TRIG_MODE_INTERNEL for internally trig
 * @return 0 - success, other - error
 */
int encoder_dev_virtual_trig(int count)
{
    int res = ioctl(encoder_dev_fd, _IOW('D', ENCODER_CMD_FUNCTION_VIRT_INPUT, 4), count);
    ON_ERROR_RET(res, "", "", -1);
    return 0;
}

/**
 * @brief Set the trig signal to internal or external.
 * @param mode ENCODER_TRIG_MODE_EXTERNEL for externally trig, or ENCODER_TRIG_MODE_INTERNEL for internally trig
 * @return 0 - success, other - error
 */
int encoder_dev_set_trigmod(int mode)
{
    int res = ioctl(encoder_dev_fd, _IOW('D', mode, 0));
    ON_ERROR_RET(res, "", "", -1);
    return 0;
}

/**
 * @brief Claer the cache in hardware encoder unit.
 * @note The frequency division counters continutly count pluses of external/internal signal.
 *       This functhion clears the counters.
 * @return 0 - success, other - error
 */
int encoder_dev_flush()
{
    int res = ioctl(encoder_dev_fd, _IOW('D', ENCODER_CMD_FUNCTION_CLEAR, 0));
    ON_ERROR_RET(res, "", "", -1);
    return 0;
}

/**
 * @brief Deinitialize the hardware encoder unit.
 * @note This function just close the file descriptor of the encoder unit.
 * @return 0 - success, other - error
 */
int encoder_dev_deinit()
{
    int res = close(encoder_dev_fd);

    ON_ERROR_RET(res, "", "", -1);
    return 0;
}
