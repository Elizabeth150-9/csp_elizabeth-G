// Elizabeth Gutierrez, First Program C
#include <stdio.h>

char name[90];
int food;
float goodbye;

int main(void){
    printf("Hi, what is your name? \n");
    scanf("%s", name);
    printf("Hello what is your favourite food? \n");
    scanf("%d", food);
    printf("Goodbye! \n");
    scanf("%f", goodbye);
    return 0;

}
