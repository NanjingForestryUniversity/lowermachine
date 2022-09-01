/**
 * @file host_computer.c
 * @brief Commnunicate with host computer. Protocal is described in hostcomputer通信协议.md
 * @author miaow (3703781@qq.com)
 * @version 1.1
 * @date 2022/08/06
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2022  miaow
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/16 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2022/08/06 <td>1.1     <td>miaow     <td>Add fifob
 * </table>
 */
#include <host_computer.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/tcp.h>
#include <stdlib.h>
#include <pthread.h>
#include <common.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <fifo_dev.h>
#include <encoder_dev.h>
#include <data_filter.h>

static char perror_buffer[128];
/**
 * @brief Queue handle structure
 */
typedef struct
{
    queue_uint64_msg_t *cmd_q;         // A pointer to the queue for commands
    int socket_fd;                     // The socket fd for receiving commands and data
    int need_exit;                     // The flag variable to indicate whether to exit the loop_thread in this file
    pthread_t loop_thread;             // The main routine of this module, which parses commands and data from host, puts them into the queue
    pthread_mutex_t loop_thread_mutex; // The mutex for loop_thread
} hostcomputer_t;

static hostcomputer_t _global_structure;
void *loop_thread_func(void *param);

/**
 * @brief Pre initialize host computer module
 * @param data_q A pointer to the queue storing the valve data from host computer
 * @param cmd_q A pointer to the queue storing the cmd from host computer
 * @return 0 - success
 */
int hostcomputer_init(queue_uint64_msg_t *cmd_q)
{
    _global_structure.cmd_q = cmd_q;

    pthread_mutex_init(&_global_structure.loop_thread_mutex, NULL);
    pthread_create(&_global_structure.loop_thread, NULL, loop_thread_func, NULL);

    return 0;
}

static void send_error(int fd)
{
    write(fd, "error", 5);
    printf("\r\nerror sent\r\n");
}

/**
 * @brief Receive `size` bytes from a socket. If no more bytes are available at the socket, this function return -1 when timeout reaches.
 * @param fd The socket fd
 * @param buf Received bytes
 * @param size Number of bytes to receive
 * @return  These calls return the number of bytes received, or -1 if time out occurred
 */
static int recvn(int fd, char *buf, int size)
{
    char *pt = buf;
    int count = size;
    while (count > 0)
    {
        int len = recv(fd, pt, count, 0);
        // if (len == -1 && (errno == EAGAIN || errno == EWOULDBLOCK))
        // {
        //     // printf("recv timeout\r\n");
        // }
        if (len == -1)
            return -1;
        else if (len == 0)
            return size - count;
        pt += len;
        count -= len;
    }
    return size;
}

/**
 * @brief To inspect the status of TCP connection
 * @param sock_fd The socket
 * @return 0 - Not connected, 1 - connected
 */
static int is_connected(int sock_fd)
{
    struct tcp_info info;
    int len = sizeof(info);
    getsockopt(sock_fd, IPPROTO_TCP, TCP_INFO, &info, (socklen_t *)&len);
    return info.tcpi_state == TCP_ESTABLISHED;
}

/**
 * @brief This function runs in child thread and handles communication with host computer
 * @param param NULL
 * @return NULL
 */
void *loop_thread_func(void *param)
{
    // printf("loop thread in %s start\r\n", __FILE__);
    int need_exit = 0, frame_count = 0, error_sent = 0;
    int std_count, empty_packets_num = 0;
    int empty_count_initial = 0;
    int empty_count_processed = 0;
    char pre;
    uint16_t n_bytes;
    char type[2];
    char data[HOST_COMPUTER_PICTURE_BYTES + 1];
    char check[2];
    datafilter_typedef datafilter;

    while (!need_exit)
    {
        pthread_mutex_lock(&_global_structure.loop_thread_mutex);
        need_exit = _global_structure.need_exit;
        pthread_mutex_unlock(&_global_structure.loop_thread_mutex);
        // reconnect if not connected
        if (!is_connected(_global_structure.socket_fd))
        {
            _global_structure.socket_fd = socket(AF_INET, SOCK_STREAM, 0);
            struct timeval timeout = {.tv_sec = 10, .tv_usec = 0};
            setsockopt(_global_structure.socket_fd, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout));
            ON_ERROR_RET(_global_structure.socket_fd, "hostcomputer_init", "", NULL);
            struct sockaddr_in serAddr;
            serAddr.sin_family = AF_INET;
            // serAddr.sin_addr.s_addr = inet_addr(HOST_COMPUTER_IP);
            inet_pton(AF_INET, HOST_COMPUTER_IP, &serAddr.sin_addr);
            serAddr.sin_port = htons(HOST_COMPUTER_PORT);
            printf("Connecting host computer...");
            fflush(stdout);
            if (connect(_global_structure.socket_fd, (struct sockaddr *)&serAddr, sizeof(struct sockaddr_in)) == -1)
            {
                sleep(2);
                close(_global_structure.socket_fd);
                printf("FAILED\r\n");
                continue;
            }
            printf("OK\r\n");
        }

        // =======================parse the protocol=========================================

        if (recvn(_global_structure.socket_fd, (char *)&pre, 1) > 1)
        {
            // close(_global_structure.socket_fd);
            printf("pre_len!=1\r\n");
            continue;
        }
        if (pre != 0xAA)
        {
            // close(_global_structure.socket_fd);
            // printf("%X ", (int)pre);
            // fflush(stdout);
            continue;
        }
        if (recvn(_global_structure.socket_fd, (char *)&n_bytes, 2) != 2)
        {
            // close(_global_structure.socket_fd);
            printf("n_bytes_len!=2\r\n");
            continue;
        }
        n_bytes = ntohs(n_bytes);
        if (n_bytes != HOST_COMPUTER_PICTURE_BYTES + 2 && n_bytes > 10)
        {
            // close(_global_structure.socket_fd);
            printf("n_bytes> 10 and n_bytes!=HOST_COMPUTER_PICTURE_BYTES + 2\r\n");
            continue;
        }
        if (recvn(_global_structure.socket_fd, (char *)type, 2) != 2)
        {
            // close(_global_structure.socket_fd);
            printf("type!=2\r\n");
            continue;
        }
        if (recvn(_global_structure.socket_fd, (char *)data, n_bytes - 2) != n_bytes - 2)
        {
            // close(_global_structure.socket_fd);
            printf("data_len!=n_bytes-2\r\n");
            continue;
        }

        data[n_bytes - 2] = 0;
        if (recvn(_global_structure.socket_fd, (char *)check, 2) != 2)
        {
            // close(_global_structure.socket_fd);
            printf("check_len!=2\r\n");
            continue;
        }
        if (recvn(_global_structure.socket_fd, (char *)&pre, 1) != 1)
        {
            // close(_global_structure.socket_fd);
            printf("end_len!=1\r\n");
            continue;
        }
        if (pre != 0xBB)
        {
            // close(_global_structure.socket_fd);
            printf("end!=0xBB\r\n");
            continue;
        }

        // =======================parse the commands=========================================
        // commands are reformed as an uint64_t, 0x--------xxxxxxxx, where `-` refers its paramter and `x` is HOSTCOMPUTER_CMD
        if (type[0] == 'd' && type[1] == 'a')
        {
            /*
            int current_count = fifo_dev_get_count();
            int current_count_filtered = datafilter_calculate(&datafilter_a, current_count);

            if (++frame_count_a > HOST_COMPUTER_BEGINNING_PICTURES_IGNORE_NUM)
            {
                fifo_dev_write_frame(data, 0);
            }
            int added_count = fifo_dev_get_count();
            printf("before %d->after %d, diff %d, filter %d\r\n", current_count, added_count, added_count - current_count, current_count_filtered);
            */
            //=================================================
            
            int current_count, current_count_filtered, diff_count, empty_count_to_process;
            if (n_bytes - 2 != HOST_COMPUTER_PICTURE_BYTES)
            {
                printf("n_bytes-2!=%d\r\n", HOST_COMPUTER_PICTURE_BYTES);
                continue;
            }
            // get the item counts and its slide average value
            current_count = fifo_dev_get_count();
            current_count_filtered = datafilter_calculate(&datafilter, current_count);
            frame_count++;
            if (frame_count == HOST_COMPUTER_PICTURES_BEGINNING_IGNORE_NUM + 1)
            {
                empty_count_initial = fifo_dev_get_emptycount();
            }
            else if (frame_count == 100) // record the normal item counts in fifo
            {
                std_count = current_count_filtered;
            }
            if (frame_count > HOST_COMPUTER_PICTURES_BEGINNING_IGNORE_NUM)
            {
                // do nothing at first two frames, because that the first frame is set to zero and was concatenated to the delay frame before
                // in case of late arrival of the first two frames.
                empty_count_to_process = fifo_dev_get_emptycount() - empty_count_initial - empty_count_processed;
                if (empty_count_to_process >= HOST_COMPUTER_PICTURE_ROW_NUM)
                {
                    empty_count_processed += HOST_COMPUTER_PICTURE_ROW_NUM;
                }
                else
                {
                    fifo_dev_write_frame(data, empty_count_to_process);
                    empty_count_processed += empty_count_to_process;
                }
            }
            if (current_count == 0)
                empty_packets_num++;
            else
                empty_packets_num = 0;
            
            
            // print fifo status
            printf("a ||| %d | cnt %d | avgcnt %d | stdcnt %d",
                   frame_count, current_count, current_count_filtered, std_count);
            fflush(stdout);
            // if (empty_count_to_process)
                printf(" ||| initemp %d | toprc %d | prcd %d\r\n", empty_count_initial,
                       empty_count_to_process, empty_count_processed);
            // else
                // printf("\r\n");
            // if the item counts changes a lot compared with normal counts,
            // meaning something goes wrong, a message will send to the hostcomputer
            diff_count = current_count_filtered - std_count;
            int diff_cond = diff_count > 250 || diff_count < -250;
            int frame_count_cond = frame_count > 100;
            int empty_packets_cond = empty_packets_num >= 5;

            if (((frame_count_cond && diff_cond) || empty_packets_cond) && !error_sent)
            {
                error_sent = 1;
                printf("\r\na ||| avgcnt %d | %d larger", current_count_filtered, diff_count);
                fflush(stdout);
                send_error(_global_structure.socket_fd);
            }
        }
        else if (type[0] == 's' && type[1] == 't')
        {
            // printf("Start put to cmd queue, param:%d\r\n", (int)atoll(data));
            frame_count = 0;
            error_sent = 0;
            empty_packets_num = 0;
            std_count = 0;
            datafilter_deinit(&datafilter);
            datafilter_init(&datafilter, 20);
            empty_count_processed = 0;
            empty_count_initial = 0;

            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_START);
        }
        else if (type[0] == 's' && type[1] == 'p')
        {
            // printf("Stop put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_STOP);
        }
        else if (type[0] == 't' && type[1] == 'e')
        {
            // printf("Test put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_TEST);
        }
        else if (type[0] == 't' && type[1] == 't')
        {
            // printf("Test put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_STOP_TEST);
        }
        else if (type[0] == 'p' && type[1] == 'o')
        {
            // printf("Power on put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_POWERON);
        }
        else if (type[0] == 's' && type[1] == 'c')
        {
            // printf("Set camera triggle pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT);
        }
        else if (type[0] == 's' && type[1] == 'v')
        {
            // printf("Set valve pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETVALVETRIGPULSECOUNT);
        }
        else if ((type[0] == 's' && type[1] == 'd'))
        {
            // printf("Set camera to valve pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETCAMERATOVALVEPULSECOUNT);
        }
    }
    printf("loop thread in %s exit\r\n", __FILE__);
    return NULL;
}

/**
 * @brief Deinitialize and release resources used by host computer module
 * @return int
 */
int hostcomputer_deinit()
{
    pthread_mutex_lock(&_global_structure.loop_thread_mutex);
    _global_structure.need_exit = 1;
    pthread_mutex_unlock(&_global_structure.loop_thread_mutex);
    pthread_join(_global_structure.loop_thread, NULL);
    pthread_mutex_destroy(&_global_structure.loop_thread_mutex);

    close(_global_structure.socket_fd);
    _global_structure.socket_fd = 0;
    _global_structure.need_exit = 0;
    _global_structure.cmd_q = NULL;
    return 0;
}
