// Elizabeth Gutierrez, Time of Day in C
#include <stdio.h>
#include <time.h>

int main() {
    time_t t;
    struct tm *tm_info;

    time(&t);
    tm_info = localtime(&t);

    printf("%d\n", tm_info->tm_hour);

    if (tm_info->tm_hour <= 12) {
        printf("Good morning!\n");
    } else if (tm_info->tm_hour <= 18) {
        printf("Good afternoon!\n");
    } else {
        printf("Good evening!\n");
    }

    return 0;
}

