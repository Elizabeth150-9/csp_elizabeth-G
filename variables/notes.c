// Elizabeth Gutierrez, Variables Notes C
#include <stdio.h>

char name[20];
int age;
float pi;

int main(void){
    printf("Welcome, what is your name: \n");
    scanf("%s", name);
    printf("How old are you: \n");
    scanf("%d", age);
    printf("Write out as much pi as you know: \n");
    scanf("%f", &pi);
    printf("Hello I am %s. I am %d years old. I like the number %f.\n", name, age, pi);
    printf("%d\n", age);
    printf("%f\n", pi);
    return 0;
    
}