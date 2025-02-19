// Elizabeth Gutierrez, First Program c
#include <stdio.h>

char name[20];
char food[20];

int main(void){
    printf("Welcome, what is your name? \n");
    scanf("%s", name);
    printf("Hello %s what is your favourite food?\n", name);
    scanf("%s", food);
    printf("%s's favourite food is %s.\n", name, food);
    return 0;
}
