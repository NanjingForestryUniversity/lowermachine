/**
 * @file host_computer.c
 * @brief Commnunicate with host computer. Protocal is described in 下位机和上位机通信协议 V1.4
 * @author miaow (3703781@qq.com)
 * @version 1.2
 * @date 2023/05/07
 * @mainpage github.com/NanjingForestryUniversity
 *
 * @copyright Copyright (c) 2023  miaow
 *
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/16 <td>1.0     <td>miaow     <td>Write this file
 * <tr><td>2022/08/06 <td>1.1     <td>miaow     <td>Add fifob
 * <tr><td>2023/05/07 <td>1.2     <td>miaow     <td>Port to b03 branch 
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
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <encoder_dev.h>
#include <data_filter.h>
#include <sys/time.h>
#include <time.h>
#include <signal.h>

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
    pthread_mutex_t is_connected_mutex;
    timer_t heartbeat_timer; 
} hostcomputer_t;

static hostcomputer_t _global_structure;
void *loop_thread_func(void *param);
void heartbeat_timer_func(__sigval_t param);

/**
 * @brief Pre initialize host computer module
 * @param data_q A pointer to the queue storing the valve data from host computer
 * @param cmd_q A pointer#include <sys/time.h> to the queue storing the cmd from host computer
 * @return 0 - success
 */
int hostcomputer_init(queue_uint64_msg_t *cmd_q)
{
    struct sigevent evp;
    struct itimerspec ts;
    _global_structure.cmd_q = cmd_q;

    pthread_mutex_init(&_global_structure.loop_thread_mutex, NULL);
    pthread_mutex_init(&_global_structure.is_connected_mutex, NULL);
    pthread_create(&_global_structure.loop_thread, NULL, loop_thread_func, NULL);
    memset(&evp, 0, sizeof(evp));
    evp.sigev_value.sival_ptr = &_global_structure.heartbeat_timer;
    evp.sigev_notify = SIGEV_THREAD;
    evp.sigev_notify_function = heartbeat_timer_func;
    timer_create(CLOCK_REALTIME, &evp, &_global_structure.heartbeat_timer);
    ts.it_interval.tv_sec = 3;
    ts.it_interval.tv_nsec = 0;
    ts.it_value.tv_sec = 3;
    ts.it_value.tv_nsec = 0;
    timer_settime(_global_structure.heartbeat_timer, TIMER_ABSTIME, &ts, NULL);
    return 0;
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
    pthread_mutex_lock(&_global_structure.is_connected_mutex);
    getsockopt(sock_fd, IPPROTO_TCP, TCP_INFO, &info, (socklen_t *)&len);
    pthread_mutex_unlock(&_global_structure.is_connected_mutex);
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
    int need_exit = 0;
    char pre;
    uint32_t n_bytes;
    char type[2];
    char data[20];
    char check[2];

    while (!need_exit)
    {
        pthread_mutex_lock(&_global_structure.loop_thread_mutex);
        need_exit = _global_structure.need_exit;
        pthread_mutex_unlock(&_global_structure.loop_thread_mutex);
        // reconnect if not connected
        if (!is_connected(_global_structure.socket_fd))
        {
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_STOP);
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
        if (recvn(_global_structure.socket_fd, (char *)&n_bytes, 4) != 4)
        {
            // close(_global_structure.socket_fd);
            printf("n_bytes_len!=4\r\n");
            continue;
        }
        n_bytes = ntohl(n_bytes);
        if (n_bytes != 10 && n_bytes != 3)
        {
            // close(_global_structure.socket_fd);
            printf("n_bytes is not 10 or 3\r\n");
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
        if (type[0] == 's' && type[1] == 't')
        {
            // printf("Start put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_START);
        }
        else if (type[0] == 's' && type[1] == 'p')
        {
            // printf("Stop put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_STOP);
        }
        else if (type[0] == 'p' && type[1] == 'a')
        {
            // printf("Set camera triggle pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_A);
        }
        else if (type[0] == 'p' && type[1] == 'b')
        {
            // printf("Set camera triggle pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_B);
        }
        else if (type[0] == 'p' && type[1] == 'c')
        {
            // printf("Set camera triggle pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_C);
        }
        else if (type[0] == 'p' && type[1] == 'd')
        {
            // printf("Set camera triggle pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETCAMERATRIGPULSECOUNT_D);
        }
    }
    printf("loop thread in %s exit\r\n", __FILE__);
    return NULL;
}

void heartbeat_timer_func(__sigval_t param)
{
    static uint8_t heartbeat_packet[] = {0xaa, 0x00, 0x00, 0x00, 0x03, 'h', 'b', 0xff, 0xff, 0xff, 0xbb};
    if (is_connected(_global_structure.socket_fd))
        write(_global_structure.socket_fd, heartbeat_packet, sizeof(heartbeat_packet));
}

/**
 * @brief Deinitialize and release resources used by host computer module
 * @return int
 */
int hostcomputer_deinit()
{
    timer_delete(_global_structure.heartbeat_timer);

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
