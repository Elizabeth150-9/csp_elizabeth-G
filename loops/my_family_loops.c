// Elizabeth Gutierrez, My Family Loops in C
#include <stdio.h>

int main(void){
    int start = 0;
    char family[][80] = {"Saul", "Ingrid", "Rebeca", "Ema", "Saul"};
    printf("Hello %s, they sky is blue!\n", family);
    int mlength = sizeof(family)/sizeof(family[0]); 

    return 0;
}
