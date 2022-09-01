/**
 * @file fifo_dev.c
 * @brief Operate the hardware fifo with Linux application
 * @details Call fifo_dev_init() paired with fifo_dev_deinit() as their names imply, fifo_dev_write_xxx() can be executed several times to operate the hardware fifo between fifo_dev_init() and fifo_dev_deinit()
 * @mainpage github.com/NanjingForestryUniversity
 * @author miaow (3703781@qq.com)
 * @version 1.1
 * @date 2022/08/07
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2022  miaow
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/09 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2022/08/07 <td>1.1     <td>miaow     <td>Add ignore_row_num to fifo_dev_write_frame
 * </table>
 */

#include <fifo_dev.h>
#include <pthread.h>
#include <unistd.h>
#include <common.h>
#include <fcntl.h>
#include <host_computer.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <data_filter.h>

#define FIFO_CMD_FUNCTION_CLEAR 1
#define FIFO_CMD_FUNCTION_PADDING 2
#define FIFO_CMD_GET_EMPTYCOUNT 3

static int fifo_dev_fd = -1;
static char perror_buffer[128];

/**
 * @brief Initialize the hardware fifo
 * @note This function just open the file descriptor of the hardware fifo
 * @return 0 - success, other - error
 */
int fifo_dev_init()
{
    fifo_dev_fd = open(FIFO_DEV_PATH, O_RDWR);
    ON_ERROR_RET(fifo_dev_fd, "", "", -1);
    return 0;
}

/**
 * @brief Get the count of read operation when the fifo is empty.
 * @note The empty read count will be set to zero at fifo_dev_clear() only. 
 * @return >=0 - success, other - error
 */
int fifo_dev_get_emptycount()
{
    int count;
    int res = ioctl(fifo_dev_fd, _IOR('D', FIFO_CMD_GET_EMPTYCOUNT, 0), &count);

    ON_ERROR_RET(res, "", "", -1);
    return count;
}

/**
 * @brief Set value to put of a frame.
 * @param valve_data An array HOST_COMPUTER_PICTURE_COLUMN_BYTES bytes * HOST_COMPUTER_PICTURE_ROW_NUM rows.
 * @param ignore_row_num Remove the ignore_row_num rows at the beginning of the frame. range: [0, HOST_COMPUTER_PICTURE_BYTES)
 * @return 0 - success, other - error
 */
int fifo_dev_write_frame(void *valve_data, int ignore_row_num)
{
    ssize_t size;
    char *valve_to_write = (char *)valve_data + ignore_row_num * HOST_COMPUTER_PICTURE_COLUMN_BYTES;
    int size_to_write = HOST_COMPUTER_PICTURE_COLUMN_BYTES * (HOST_COMPUTER_PICTURE_ROW_NUM - ignore_row_num);

    size = write(fifo_dev_fd, valve_to_write, size_to_write);
    int res = -(size < size_to_write);
    ON_ERROR_RET(res, "size=", "", -1);

    return 0;
}

/**
 * @brief Set value to put of a row.
 * @param valve_data An array 32bytes.
 * @return 0 - success, other - error
 */
int fifo_dev_write_row(void *valve_data)
{
    ssize_t size = write(fifo_dev_fd, valve_data, 32);
    int res = -(size < 32);
    ON_ERROR_RET(res, "size=", "", -1);
    return 0;
}

/**
 * @brief Flush and clear the hardware fifo.
 * @return 0 - success, other - error
 */
int fifo_dev_clear()
{
    int res = ioctl(fifo_dev_fd, _IOW('D', FIFO_CMD_FUNCTION_CLEAR, 0));
    ON_ERROR_RET(res, "", "", -1);
    return 0;
}


/**
 * @brief Write `count` zero-items to the haredware fifo, which acts as delay time.
 * @param count Count of zero-items to write.
 * @return 0 - success, other - error
 */
int fifo_dev_write_delay(uint32_t count)
{
    int res = ioctl(fifo_dev_fd, _IOW('D', FIFO_CMD_FUNCTION_PADDING, 0), count);

    ON_ERROR_RET(res, "", "", -1);
    return 0;
}

/**
 * @brief Get the count of items in the hardware fifo.
 * @note An item from hardware fifo is of 256 bits in size, aka. 32 bytes, 8 integers
 * @return >=0 - success, other - error
 */
int fifo_dev_get_count()
{
    uint32_t fifo_item_count;
    ssize_t size = read(fifo_dev_fd, &fifo_item_count, sizeof(fifo_item_count));

    if (size != sizeof(fifo_item_count))
        ON_ERROR(-1, "size=", "");
    
    return fifo_item_count;
}

/**
 * @brief Deinitialize the hardware fifo.
 * @note This function just close the file descriptor of the hardware fifo.
 * @return 0 - success, -1 - error
 */
int fifo_dev_deinit()
{
    int res = close(fifo_dev_fd);

    ON_ERROR_RET(res, "", "", -1);
    return 0;
}
