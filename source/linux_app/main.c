/**
 * @file main.c
 * @brief Excute the commands from host_computer
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/06/12
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2022  miaow
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/12 <td>1.0     <td>miaow     <td>Write this file
 * </table>
 */
#include <fifo_dev.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <math.h>
#include <queue_uint64.h>
#include <encoder_dev.h>
#include <host_computer.h>
#include <memory.h>
#include <stdio.h>
#include <unistd.h>

#define SET_VALVE_ONLY_N_ON(u32_buf, n) \
    bzero(u32_buf, sizeof(u32_buf));    \
    SET_VALVE_N_ON(u32_buf, n)
#define SET_VALVE_N_ON(u32_buf, n) u32_buf[n / 32] = 1 << (n % 32)


/**
 * @brief Value of state machine
 */
typedef enum
{
    SLEEPING = 0,
    RUNNING = 1,
} status_enum_t;

queue_uint64_msg_t cmd_queue = {0};

static status_enum_t status = SLEEPING;
static int camera_trigger_pulse_count = 1200;
static int valve_trigger_pulse_count = 120;
static int camera_to_valve_pulse_count = 500;

void process_cmd(uint64_t *cmd);

/**
 * @brief Read from the cmd_queue and excute the command every 100ms.
 * @param argc not used
 * @param argv not used
 * @return int should not return.
 */
int main(int argc, char *argv[])
{
    queue_uint64_init(&cmd_queue, 9999);

    // Initialize drivers and clear all caches
    encoder_dev_init();
    encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
    encoder_dev_set_divide(2, 8);
    fifo_dev_init();

    //==test encoder================================================================
    // fifo_dev_init();
    // encoder_dev_set_trigmod(ENCODER_TRIG_MODE_EXTERNEL);
    // encoder_dev_set_divide(4, 8);
    // int a = 1;
    // while (a)
    // {
    //     printf("input a\r\n");
    //     scanf("%d", &a);
    //     printf("a=%d\r\n\r\n\r\n", a);
    // }
    // encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
    // encoder_dev_deinit();
    // queue_uint64_deinit(&cmd_queue);
    // return 0;

    //==test fifo================================================================
    // char data[HOST_COMPUTER_PICTURE_COLUMN_BYTES * HOST_COMPUTER_PICTURE_ROW_NUM + 1];
    // fifo_dev_init();
    // fifo_dev_write_frame(data);
    // printf("%d\r\n", fifo_dev_get_count());
    // fifo_dev_write_frame(data);
    // printf("%d\r\n", fifo_dev_get_count());
    // fifo_dev_clear();
    // printf("%d\r\n", fifo_dev_get_count());
    // fifo_dev_deinit();
    // encoder_dev_deinit();
    // return 0;
    //==================================================================

    fifo_dev_clear();
    hostcomputer_init(&cmd_queue);
    printf("\r\n>>>>>\r\nstatus==SLEEPING\r\n<<<<<\r\n\r\n");
    uint64_t cmd;
    int TRUE = 1;
    // Read from the cmd_queue and excute the command every 100ms
    while (TRUE)
    {
        if (queue_uint64_get(&cmd_queue, &cmd) == 0)
            process_cmd(&cmd);
        usleep(1000);
    }

    // Never run here
    hostcomputer_deinit();
    fifo_dev_clear();
    encoder_dev_set_divide(2, 8);
    encoder_dev_virtual_trig(20);

    fifo_dev_deinit();
    encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
    encoder_dev_deinit();
    queue_uint64_deinit(&cmd_queue);

    return 0;
}

/**
 * @brief Excute the command and control the states
 * @param cmd The command to be excuted
 */
void process_cmd(uint64_t *cmd)
{
    int tmp_cmd = (int)*cmd;
    int tmp_data = (int)(*cmd >> 32);

    // Only in the SLEEPING state, it resbonds to START or TEST command.
    if (status == SLEEPING)
    {
        if (tmp_cmd == HOSTCOMPUTER_CMD_START)
        {
            // Before running, clear the hardware fifo and hardware encoder. Then, the two dividers and delay value should be set.
            // Also, the hareware encoder is expected to receiving pluse of encoder: the EXTERNAL mode
            fifo_dev_clear();
            encoder_dev_flush();

            encoder_dev_set_divide(valve_trigger_pulse_count, camera_trigger_pulse_count);
            fifo_dev_write_delay(camera_to_valve_pulse_count + HOST_COMPUTER_PICTURE_ROW_NUM * HOST_COMPUTER_PICTURES_BEGINNING_IGNORE_NUM);
            encoder_dev_set_trigmod(ENCODER_TRIG_MODE_EXTERNEL);
            printf("\r\n>>>>>\r\nstatus==RUNNING\r\ncamera_trigger_pulse_count=%d\r\nvalve_trigger_pulse_count=%d\r\n"
            "camera_to_valve_pulse_count=%d\r\n<<<<<\r\n\r\n", camera_trigger_pulse_count, 
            valve_trigger_pulse_count, camera_to_valve_pulse_count + HOST_COMPUTER_PICTURE_ROW_NUM * HOST_COMPUTER_PICTURES_BEGINNING_IGNORE_NUM);
            status = RUNNING;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_TEST)
        {
            uint32_t row_data[8] = {0};
            // When to excute TEST cmd (aka testing the valve), hardware fifo and hardware encoder should be cleared.
            // A new combination of divider is set: 2 for both valve and camera, for less virtual pluse is needed to triggle valve in INTERNAL mode.
            // Note that camera can be triggled during testing.
            fifo_dev_clear();
            encoder_dev_flush();
            encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
            encoder_dev_set_divide(2, 8);  // fifo out every 8/4=2 cycle, valveboard operate every 2 cycle

            // A parameter below 256 represents a single shot, the value of parameter indicates the valve to triggle.
            if (tmp_data < 256)
            {
                SET_VALVE_ONLY_N_ON(row_data, tmp_data);
                fifo_dev_write_row(row_data);
                // delay for 15000 us and turn off the valve
                encoder_dev_virtual_trig(2);
                usleep(15000);
                encoder_dev_virtual_trig(2);
            }
            // 257 represents triggle valve from NO.1 to 256 sequenctially. This loop blocks for 25.7s.
            else if (tmp_data == 257)
            {
                for (int i = 0; i < 256; i++)
                {
                    SET_VALVE_ONLY_N_ON(row_data, i);
                    fifo_dev_write_row(row_data);
                    bzero(&row_data, sizeof(row_data));
                    fifo_dev_write_row(row_data);
                    // printf("%d,%d\r\n", fifo_dev_get_count(), fifob_dev_get_count());
                }
                for (int i = 0; i < 257; i++)
                {
                    encoder_dev_virtual_trig(2);
                    usleep(15000);
                    encoder_dev_virtual_trig(2);
                    usleep(100000 - 15000);
                    // printf("%d,%d\r\n", fifo_dev_get_count(), fifob_dev_get_count());
                }
            }
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT)
        {
            camera_trigger_pulse_count = tmp_data;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_SETVALVETRIGPULSECOUNT)
        {
            valve_trigger_pulse_count = tmp_data;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_SETCAMERATOVALVEPULSECOUNT)
        {
            camera_to_valve_pulse_count = tmp_data;
        }
    }
    // Only in RUNNING state, the lower machine responds to STOP command.
    else if (status == RUNNING)
    {
        if (tmp_cmd == HOSTCOMPUTER_CMD_STOP)
        { 
            // Clear hardware fifo.
            // 10 virtual triggles in internal mode ensure valve is turned off.
            // Hardware encoder is flushed for a fresh start.
            fifo_dev_clear();
            encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
            encoder_dev_set_divide(4, 4);
            encoder_dev_virtual_trig(20);
            encoder_dev_flush();
            status = SLEEPING;
            printf("\r\n>>>>>\r\nstatus==SLEEPING\r\n<<<<<\r\n\r\n");
        }
    }
}
