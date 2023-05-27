/**
 * @file main.c
 * @brief Excute the commands from host_computer
 * @author miaow (3703781@qq.com)
 * @version 1.2
 * @date 2023/05/27
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2023  miaow
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/06/12 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2023/05/07 <td>1.1     <td>miaow     <td>Port to b03
 * <tr><td>2023/05/27 <td>1.2     <td>miaow     <td>Fix bug caused by the missing encoder_dev_set_clrmod()
 * </table>
 */
#include <sys/socket.h>
#include <arpa/inet.h>
#include <math.h>
#include <queue_uint64.h>
#include <encoder_dev.h>
#include <host_computer.h>
#include <memory.h>
#include <stdio.h>
#include <unistd.h>

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
typedef struct
{
    uint32_t a;
    uint32_t b;
    uint32_t c;
    uint32_t d;
} camera_trigger_pulse_count_typedef;

camera_trigger_pulse_count_typedef camera_trigger_pulse_count = {
    .a = 100,
    .b = 100,
    .c = 100,
    .d = 100};

void process_cmd(uint64_t *cmd);

/**
 * @brief Read from the cmd_queue and excute the command every 100ms.
 * @param argc not used
 * @param argv not used
 * @return int should not return.
 */
int main(int argc, char *argv[])
{
    uint64_t cmd;
    queue_uint64_init(&cmd_queue, 9999);

    // Initialize drivers and clear all caches
    encoder_dev_init();
    encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
    encoder_dev_set_divide(8, 8, 8, 8);

    hostcomputer_init(&cmd_queue);
    printf("\r\n>>>>>\r\nstatus==SLEEPING\r\n<<<<<\r\n\r\n");

    // Read from the cmd_queue and excute the command every 100ms
    while (1)
    {
        if (queue_uint64_get(&cmd_queue, &cmd) == 0)
            process_cmd(&cmd);
        usleep(1000);
    }

    // Never run here
    hostcomputer_deinit();
    encoder_dev_set_divide(100,100,100,100);
    encoder_dev_virtual_trig(20);

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
            encoder_dev_flush();

            encoder_dev_set_divide(camera_trigger_pulse_count.a,
                                   camera_trigger_pulse_count.b,
                                   camera_trigger_pulse_count.c,
                                   camera_trigger_pulse_count.d);

            encoder_dev_set_trigmod(ENCODER_TRIG_MODE_EXTERNEL);
            encoder_dev_set_clrmod(ENCODER_CLEAR_MODE_BOTH);
            printf("\r\n>>>>>\r\nstatus==RUNNING\r\ncamera_a=%d\r\ncamera_b=%d\r\ncamera_c=%d\r\ncamera_d=%d\r\n<<<<<\r\n\r\n",
                   camera_trigger_pulse_count.a,
                   camera_trigger_pulse_count.b,
                   camera_trigger_pulse_count.c,
                   camera_trigger_pulse_count.d);
            status = RUNNING;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_A)
        {
            camera_trigger_pulse_count.a = tmp_data;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_B)
        {
            camera_trigger_pulse_count.b = tmp_data;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_C)
        {
            camera_trigger_pulse_count.c = tmp_data;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_D)
        {
            camera_trigger_pulse_count.d = tmp_data;
        }
    }
    // Only in RUNNING state, the lower machine responds to STOP command.
    else if (status == RUNNING)
    {
        if (tmp_cmd == HOSTCOMPUTER_CMD_STOP)
        {
            // Hardware encoder is flushed for a fresh start.
            encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
            encoder_dev_set_divide(4, 4, 4, 4);
            encoder_dev_virtual_trig(20);
            encoder_dev_flush();
            status = SLEEPING;
            printf("\r\n>>>>>\r\nstatus==SLEEPING\r\n<<<<<\r\n\r\n");
        }
    }
} 
