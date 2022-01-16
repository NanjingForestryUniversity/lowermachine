#include <valve.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <math.h>
#include <queue_uint64.h>
#include <camera_trigger.h>
#include <encoder.h>
#include <host_computer.h>

/**
 * @brief Value of state machine
 */
typedef enum
{
    NOT_INITIALIZED = 0,
    INITIALIZED = 1,
    RUNNING = 2,
    SLEEPING = 3,
    STOPPED = 4
} status_enum_t;

valvedata_t valvedata = {0};
queue_uint64_msg_t data_queue = {0};
queue_uint64_msg_t cmd_queue = {0};

static int count_valve = 1, count_camera = 0, count_valve_should_be = 2;
static uint64_t count_continues = 0UL, count_valve_continues = 0UL, count_camera_continues = 0UL;
static status_enum_t status = NOT_INITIALIZED;
static int camera_trigger_pulse_count = 0;
static int valve_should_trigger_pulse_count = 0;
static int valve_trigger_pulse_count = 0;
static int camera_to_valve_pulse_count = 0;

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
    // valve_test(200.0f);
    // printf("OK\r\n");
    // valve_deinit();

    hostcomputer_init(&data_queue, &cmd_queue);
    uint64_t cmd;
    int TRUE = 1;
    while (TRUE)
    {
        if (queue_uint64_get(&cmd_queue, &cmd) == 0)
        {
            process_cmd(&cmd);
            usleep(100000);
        }
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
            valve_should_trigger_pulse_count = camera_trigger_pulse_count / HOST_COMPUTER_PICTURE_ROW_NUM;
            for (int i = 0; i < camera_to_valve_pulse_count * HOST_COMPUTER_PICTURE_ROW_NUM / camera_trigger_pulse_count; i++)
                queue_uint64_put(&data_queue, 0);
            valve_init();
            cameratrigger_init();
            encoder_init(on_encoder);
            status = RUNNING;
            printf("\r\n>>>>>\r\nstatus==RUNNING\r\n<<<<<\r\n\r\n");
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_TEST)
        {
            valve_init();
            valve_test(500.0f);
            valve_deinit();
        }
    }
    else if (status == NOT_INITIALIZED)
    {
        if (tmp_cmd == HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT)
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
        else if (tmp_cmd == HOSTCOMPUTER_CMD_TEST)
        {
            valve_init();
            valve_test(500.0f);
            valve_deinit();
        }
        if (camera_trigger_pulse_count != 0 && valve_trigger_pulse_count != 0 && camera_to_valve_pulse_count != 0)
        {
            status = INITIALIZED;
            printf("\r\n>>>>>\r\nstatus==INITIALIZED\r\ncamera_trigger_pulse_count=%d\r\nvalve_trigger_pulse_count=%d\r\ncamera_to_valve_pulse_count=%d\r\n<<<<<\r\n\r\n", camera_trigger_pulse_count, valve_trigger_pulse_count, camera_to_valve_pulse_count);
        }
    }
    else if (status == INITIALIZED)
    {
        if (tmp_cmd == HOSTCOMPUTER_CMD_START)
        {
            valve_should_trigger_pulse_count = camera_trigger_pulse_count / HOST_COMPUTER_PICTURE_ROW_NUM;
            printf("valve_should_trigger_pulse_count=%d", valve_should_trigger_pulse_count);
            for (int i = 0; i < camera_to_valve_pulse_count * HOST_COMPUTER_PICTURE_ROW_NUM / camera_trigger_pulse_count; i++)
                queue_uint64_put(&data_queue, 0);
            valve_init();
            cameratrigger_init();
            encoder_init(on_encoder);
            status = RUNNING;
            printf("\r\n>>>>>\r\nstatus==RUNNING\r\n<<<<<\r\n\r\n");
        }
        else if (tmp_cmd == HOSTCOMPUTER_CMD_TEST)
        {
            valve_init();
            valve_test(500.0f);
            valve_deinit();
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
            status = SLEEPING;
            printf("\r\n>>>>>\r\nstatus==SLEEPING\r\n<<<<<\r\n\r\n");
        }
    }
}

void valve_test(float ms_for_each_channel)
{
    uint64_t valve_data = 1ul;
    for (int i = 0; i < 48; i++)
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

    if (++count_valve == valve_trigger_pulse_count + 1)
    {
        count_valve = 1;
        count_valve_continues++;
        valve_sendmsg(&valvedata);

        // printf("data:%llx send to valve, queue length is %d\r\n", valvedata.valvedata_1, data_queue.nData);
        // printf("%016llx ", valvedata.valvedata_1);
        fflush(stdout);
    }

    if (++count_valve_should_be == valve_should_trigger_pulse_count + 2)
    {
        count_valve_should_be = 2;
        valvedata.valvedata_1 = 0;
        queue_uint64_get(&data_queue, &(valvedata.valvedata_1));
        // if (data_queue.nData == 0)
        // {
        //     printf("sb\r\n");
        // }
    }

    if (++count_camera == camera_trigger_pulse_count)
    {
        // printf("camera triggled\r\n");
        count_camera = 0;
        count_camera_continues++;
        cameratrigger_trig();
    }
}
