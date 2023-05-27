/**
 * @file encoder_dev.c
 * @brief Manage the hardware encoder unit
 * @author miaow, lyz (3703781@qq.com)
 * @version 0.11
 * @date 2022/04/26
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2023  miaow, lyz
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/11 <td>0.9     <td>Miaow    <td>Write this module
 * <tr><td>2022/04/11 <td>0.10    <td>lyz      <td>Add seprate dividers up to 4 cameras
 * <tr><td>2023/04/26 <td>0.11    <td>Miaow    <td>Add Clear mode
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

static struct
{
    uint32_t valve_divide_value;
    uint32_t camera_a_divide_value;
    uint32_t camera_b_divide_value;
    uint32_t camera_c_divide_value;
    uint32_t camera_d_divide_value;
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
    encoder_dev_set_divide(100, 100, 100, 100, 100);
    return 0;
}

/**
 * @brief Set the two divider in the hareware encoder unit.
 * @param camera_a_divide the frequency division factor between the encoder signal and camera a triggle signal
 *                      Set ENCODER_DEV_DIVIDE_NOT_TO_SET to skip changing the division facter
 * @param camera_b_divide the frequency division factor between the encoder signal and camera b triggle signal
 *                      Set ENCODER_DEV_DIVIDE_NOT_TO_SET to skip changing the division facter
 * @param camera_c_divide the frequency division factor between the encoder signal and camera c triggle signal
 *                      Set ENCODER_DEV_DIVIDE_NOT_TO_SET to skip changing the division facter
 * @param camera_d_divide the frequency division factor between the encoder signal and camera d triggle signal
 *                      Set ENCODER_DEV_DIVIDE_NOT_TO_SET to skip changing the division facter
 * @return 0 - success, other - error
 */
int encoder_dev_set_divide(int camera_a_divide,
                           int camera_b_divide,
                           int camera_c_divide,
                           int camera_d_divide)
{
    if (valve_divide != ENCODER_DEV_DIVIDE_NOT_TO_SET)
        encoder_dev_divide_value_structure.valve_divide_value = 100;
    if (camera_a_divide != ENCODER_DEV_DIVIDE_NOT_TO_SET)
        encoder_dev_divide_value_structure.camera_a_divide_value = camera_a_divide;
    if (camera_b_divide != ENCODER_DEV_DIVIDE_NOT_TO_SET)
        encoder_dev_divide_value_structure.camera_b_divide_value = camera_b_divide;
    if (camera_c_divide != ENCODER_DEV_DIVIDE_NOT_TO_SET)
        encoder_dev_divide_value_structure.camera_c_divide_value = camera_c_divide;
    if (camera_d_divide != ENCODER_DEV_DIVIDE_NOT_TO_SET)
        encoder_dev_divide_value_structure.camera_d_divide_value = camera_d_divide;

    ssize_t size = write(encoder_dev_fd, &encoder_dev_divide_value_structure, sizeof(encoder_dev_divide_value_structure));
    int res = -(size != sizeof(encoder_dev_divide_value_structure));
    ON_ERROR_RET(res, "size=", "", -1);

    return 0;
}

/**
 * @brief Set the trig signal to internal or external.
 * @param count the count of virtual trig cycles.
 * @return 0 - success, other - error
 */
int encoder_dev_virtual_trig(int count)
{
    int res = ioctl(encoder_dev_fd, _IOW('D', ENCODER_CMD_FUNCTION_VIRT_INPUT, int), count);
    ON_ERROR_RET(res, "", "", -1);
    return 0;
}

/**
 * @brief Set the trig signal to internal or external.
 * @param mode ENCODER_TRIG_MODE_EXTERNEL for externally trig, or ENCODER_TRIG_MODE_INTERNEL for internally trig
 * @return 0 - success, other - error
 */
int encoder_dev_set_trigmod(encoder_dev_trig_mode_enum mode)
{
    int res = ioctl(encoder_dev_fd, _IOW('D', mode, int));
    ON_ERROR_RET(res, "", "", -1);
    return 0;
}

/**
 * @brief Set the clr signal to internal or both external and internal.
 * @return 0 - success, other - error
 */
int encoder_dev_set_clrmod(encoder_dev_clear_mode_enum mode)
{
    int res = ioctl(encoder_dev_fd, _IOW('D', mode, int));
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

