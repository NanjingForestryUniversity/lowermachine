/**
 * @file host_computer.c
 * @brief Commnunicate with host computer. Protocal is described in hostcomputer通信协议.md
 * @author miaow (3703781@qq.com)
 * @version 1.0
 * @date 2022/01/16
 * @mainpage github.com/NanjingForestryUniversity
 * 
 * @copyright Copyright (c) 2022  miaow
 * 
 * @par Changelog:
 * <table>
 * <tr><th>Date       <th>Version <th>Author  <th>Description
 * <tr><td>2022/01/16 <td>1.0     <td>miaow     <td>Write this file
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

#define HOST_COMPUTER_PICTURE_COLUMN_BYTES (HOST_COMPUTER_PICTURE_COLUMN_NUM / 8)
#define HOST_COMPUTER_RAW_DATA_BYTES (HOST_COMPUTER_PICTURE_COLUMN_BYTES * HOST_COMPUTER_PICTURE_ROW_NUM)

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
    printf("loop thread in %s start\r\n", __FILE__);
    int need_exit = 0;
    char pre;
    uint16_t n_bytes;
    char type[2];
    char data[HOST_COMPUTER_RAW_DATA_BYTES + 1];
    char check[2];
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
        if (n_bytes != HOST_COMPUTER_RAW_DATA_BYTES + 2 && n_bytes > 10)
        {
            // close(_global_structure.socket_fd);
            printf("n_bytes> 10 and n_bytes!=HOST_COMPUTER_RAW_DATA_BYTES + 2\r\n");
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
            // printf("%dbytes of data put to data queue\r\n", (int)n_bytes - 2);
            if (n_bytes - 2 != HOST_COMPUTER_RAW_DATA_BYTES)
            {
                printf("n_bytes-2!=%d\r\n", HOST_COMPUTER_RAW_DATA_BYTES);
                continue;
            }
            fifo_dev_write_frame(data);
        }
        else if (type[0] == 's' && type[1] == 't')
        {
            // printf("Start put to cmd queue, param:%d\r\n", (int)atoll(data));
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
        else if (type[0] == 's' && type[1] == 'd')
        {
            // printf("Set camera to valve pulse count put to cmd queue, param:%d\r\n", (int)atoll(data));
            queue_uint64_put(_global_structure.cmd_q, (atoll(data) << 32) | HOSTCOMPUTER_CMD_SETCAMERATOVALVEPULSECOUNT);
        }
        else
        {
            printf("Unknown command received");
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
