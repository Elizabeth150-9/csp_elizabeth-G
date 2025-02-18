// Elizabeth Gutierrez, Name Decorator C
#include <stdio.h>

char subject[19];

int main(void){
    printf("Name:\n");
    scanf("%s", subject);
    char one[] = ":):):)";
    char two[] = "Elizabeth";
    char three[] = ":):):)";
    printf("%s", one);
    int strcat(one, two);
    printf("%s", two);
    int strcat(two, three);
    printf("%s", three);
    return 0;
}