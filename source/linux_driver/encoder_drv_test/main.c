#include "encoder_dev.h"
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

static void sig_handler(int sig);

int main(int argc, char *argv[])
{
    unsigned int a = 100, b = 100, c = 100, d = 100;
    unsigned int divider = 0;
    char which[32] = {0};
    char clear_mode[32] = {0};
    encoder_dev_init();
    encoder_dev_set_trigmod(ENCODER_TRIG_MODE_EXTERNEL);
    encoder_dev_set_divide(100, 100, 100, 100, 100);
    signal(SIGINT, (sig_t)sig_handler);
    while (1)
    {
        while (strcmp(clear_mode, "i") && strcmp(clear_mode, "ei"))
        {
            printf("clear mode(i/ei)? ");
            scanf("%s", clear_mode);
        }
        
        if (strcmp(clear_mode, "i"))
        {
            encoder_dev_set_clrmod(ENCODER_CLEAR_MODE_INTERNAL);
        }     
        else
        {
            encoder_dev_set_clrmod(ENCODER_CLEAR_MODE_BOTH);
        }
        
        while (strcmp(which, "a") && strcmp(which, "b") && strcmp(which, "c") && strcmp(which, "d") && strcmp(which, "all"))
        {
            printf("which camera(a/b/c/d/all)? ");
            scanf("%s", which);
        }

        printf("divider value?(2~2^32-1)? ");
        scanf("%ud", &divider);
        if (strcmp(which, "a") == 0)
        {
            a = divider;
        }
        else if (strcmp(which, "b") == 0)
        {
            b = divider;
        }
        else if (strcmp(which, "c") == 0)
        {
            c = divider;
        }
        else if (strcmp(which, "d") == 0)
        {
            d = divider;
        }
        else if (strcmp(which, "all") == 0)
        {
            a = b = c = d = divider;
        }
        encoder_dev_set_divide(500, a, b, c, d);
        printf("clear mode is %s, divider of camera %s is set to %d\r\n\r\n", clear_mode, which, divider);
        which[0] = '\0';
        clear_mode[0] = '\0';
    }
}

static void sig_handler(int sig)
{
    encoder_dev_set_trigmod(ENCODER_TRIG_MODE_INTERNEL);
    encoder_dev_deinit();
    printf("\r\n\r\nExisting...");
    exit(0);
}