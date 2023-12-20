/**
 * main.c
*/

#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include <test_file.h>

void app_main(void)
{
    int i = 0;
    while (1) {
        printf("[%d] Hello world!\n", i);
        i++;
        do_nothing();
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
