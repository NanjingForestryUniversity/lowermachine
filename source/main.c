/**
 * @file main.c
 * @brief Excuting commands, resample data, triggle camera, and send data to valve
 * @author miaow (3703781@qq.com)
 * @version 1.1
 * @date 2023/02/08
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/16 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2023/02/08 <td>1.1     <td>miaow     <td>Add debug option for interval of camera triggle
 * </table>
 */
#include <valve.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <math.h>
#include <main.h>
#include <queue_uint64.h>
#include <camera_trigger.h>
#include <encoder.h>
#include <host_computer.h>

/**
 * @brief Value of state machine
 */
typedef enum
{
    SLEEPING = 0,
    RUNNING = 1,
} status_enum_t;

valvedata_t valvedata = {0};
queue_uint64_msg_t data_queue = {0};
queue_uint64_msg_t cmd_queue = {0};

static int count_valve = 1, count_camera = 0, count_valve_should_be = 2;
static uint64_t count_continues = 0UL, count_valve_continues = 0UL, count_camera_continues = 0UL;
static status_enum_t status = SLEEPING;
static int camera_trigger_pulse_count = 500;
static int valve_should_trigger_pulse_count = 1;
static int valve_trigger_pulse_count = 10;
static int camera_to_valve_pulse_count = 3015;
#if defined(DEBUG_CAMERA_TRIG_PERIOD)
static struct timeval tv;
static uint64_t camera_period_interval_last_us = 0UL;
static uint64_t camera_period_interval_us = 0UL;
#endif

#define ROTATE_UINT64_RIGHT(x, n) ((x) >> (n)) | ((x) << ((64) - (n)))
#define ROTATE_UINT64_LEFT(x, n) ((x) << (n)) | ((x) >> ((64) - (n)))

void on_encoder(void);
void valve_test(float ms_for_each_channel);
void valve_test2(float ms_for_each_channel, int which_channel);
void valve_test3(float ms_for_each_channel);
void process_cmd(uint64_t *cmd);

int main(int argc, char *argv[])
{
    queue_uint64_init(&data_queue, 99999);
    queue_uint64_init(&cmd_queue, 99999);

    // valve_init();
    // printf("testing valve.....");
    // fflush(stdout);
    // valve_test3(100.0f);
    // valve_test2(200.0f, 0);
    // for (int i = 0; i < 999; i++)
    // {
    //     valve_test(200.0f);
    // }
    // printf("OK\r\n");
    // valve_deinit();

    hostcomputer_init(&data_queue, &cmd_queue);
    printf("\r\n>>>>>\r\nstatus==SLEEPING\r\n<<<<<\r\n\r\n");
    uint64_t cmd;
    int TRUE = 1;
    while (TRUE)
    {
        if (queue_uint64_get(&cmd_queue, &cmd) == 0)
        {
            process_cmd(&cmd);
        }
        usleep(100000);
    }
    hostcomputer_deinit();
    queue_uint64_deinit(&data_queue);
    queue_uint64_deinit(&cmd_queue);
    return 0;
}

void process_cmd(uint64_t *cmd)
{
    int tmp_cmd = (int)*cmd;
    int tmp_data = (int)(*cmd >> 32);
    if (status == SLEEPING)
    {
        if (tmp_cmd == HOSTCOMPUTER_CMD_START)
        {
            queue_uint64_clear(&data_queue);
            valve_should_trigger_pulse_count = camera_trigger_pulse_count / HOST_COMPUTER_PICTURE_ROW_NUM;
            for (int i = 0; i < camera_to_valve_pulse_count * HOST_COMPUTER_PICTURE_ROW_NUM / camera_trigger_pulse_count; i++)
                queue_uint64_put(&data_queue, 0L);

            valve_init();
            cameratrigger_init();
            encoder_init(on_encoder);
            printf("\r\n>>>>>\r\nstatus==RUNNING\r\ncamera_trigger_pulse_count=%d\r\nvalve_trigger_pulse_count=%d\r\ncamera_to_valve_pulse_count=%d\r\n<<<<<\r\n\r\n", camera_trigger_pulse_count, valve_trigger_pulse_count, camera_to_valve_pulse_count);
            status = RUNNING;
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_TEST)
        {
            valve_init();
            valve_test(500.0f);
            valve_deinit();
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
    else if (status == RUNNING)
    {
        if (tmp_cmd == HOSTCOMPUTER_CMD_STOP)
        {
            encoder_deinit();
            cameratrigger_deinit();
            valve_deinit();
            queue_uint64_clear(&data_queue);
#if defined(DEBUG_CAMERA_TRIG_PERIOD)
            printf("\r\n>>>>>\r\nstatus==SLEEPING\r\ncamera_period_us=%.2f\r\n<<<<<\r\n\r\n", (float)camera_period_interval_us / (float)(count_camera_continues - 1));
            camera_period_interval_us = 0UL;
            camera_period_interval_last_us = 0UL;
#else
            printf("\r\n>>>>>\r\nstatus==SLEEPING\r\n<<<<<\r\n\r\n");
#endif
            count_continues = 0UL;
            count_valve_continues = 0UL;
            count_camera_continues = 0UL;
            count_camera = 0;
            count_valve = 1;
            count_valve_should_be = 2;

            status = SLEEPING;
        }
    }
}

void valve_test(float ms_for_each_channel)
{
    uint64_t valve_data = 1ul;

    for (int i = 0; i < HOST_COMPUTER_PICTURE_COLUMN_NUM; i++)
    {
        usleep((useconds_t)(ms_for_each_channel * 500.0f));
        valvedata.valvedata_1 = valve_data << i;
        valve_sendmsg(&valvedata);
        usleep((useconds_t)(ms_for_each_channel * 500.0f));
        valvedata.valvedata_1 = 0;
        valve_sendmsg(&valvedata);
    }
}

void valve_test2(float ms_for_each_channel, int which_channel)
{
    uint64_t valve_data = 1ul;
    for (int i = 0; i < 10; i++)
    {
        usleep((useconds_t)(ms_for_each_channel * 500.0f));
        valvedata.valvedata_1 = valve_data << which_channel;
        valve_sendmsg(&valvedata);
        usleep((useconds_t)(ms_for_each_channel * 500.0f));
        valvedata.valvedata_1 = 0;
        valve_sendmsg(&valvedata);
    }
}

void valve_test3(float ms_for_each_channel)
{
    valvedata.valvedata_1 = 0x5555555555555555ul;
    for (int i = 0; i < 9999; i++)
    {
        usleep((useconds_t)(ms_for_each_channel * 250.0f));
        valvedata.valvedata_1 = 0x5555555555555555ul;
        valve_sendmsg(&valvedata);
        usleep((useconds_t)(ms_for_each_channel * 250.0f));

        valvedata.valvedata_1 = 0;
        valve_sendmsg(&valvedata);
        usleep((useconds_t)(ms_for_each_channel * 250.0f));

        valvedata.valvedata_1 = 0xaaaaaaaaaaaaaaaaul;
        valve_sendmsg(&valvedata);
        usleep((useconds_t)(ms_for_each_channel * 250.0f));

        valvedata.valvedata_1 = 0;
        valve_sendmsg(&valvedata);
        usleep((useconds_t)(ms_for_each_channel * 250.0f));
    }
}

void on_encoder()
{
    count_continues++;

    // send resampled data to valve, the resample cycle is valve_trigger_pulse_count
    if (++count_valve == valve_trigger_pulse_count + 1)
    {
        count_valve = 1;
        count_valve_continues++;
        valve_sendmsg(&valvedata);
    }

    // load valve data to valvedata structure
    if (++count_valve_should_be == valve_should_trigger_pulse_count + 2)
    {
        count_valve_should_be = 2;
        valvedata.valvedata_1 = 0;
        queue_uint64_get(&data_queue, &(valvedata.valvedata_1));
    }

    //  triggle camera in a cycle of camera_trigger_pulse_count
    if (++count_camera == camera_trigger_pulse_count)
    {
        count_camera = 0;
        count_camera_continues++;
#if defined(DEBUG_CAMERA_TRIG_PERIOD)
        gettimeofday(&tv, NULL);
        if (camera_period_interval_last_us != 0UL)
            camera_period_interval_us += ((uint64_t)tv.tv_sec * 1000000 + (uint64_t)tv.tv_usec) - camera_period_interval_last_us;
        camera_period_interval_last_us = ((uint64_t)tv.tv_sec * 1000000 + (uint64_t)tv.tv_usec);
#endif

        cameratrigger_trig();
    }
}
