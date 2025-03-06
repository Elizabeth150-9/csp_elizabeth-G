// Elizabeth Gutierrez, My Family Loops in C
#include <stdio.h>

int main(void){
    int start = 0; 
    char family[][80] = {"Saul", "Ingrid", "Rebeca", "Betel", "Ema", "Saul"};
    while(start <70){
    printf("Hello %s, the sky is blue!\n", family);
    start++;
    }
    

    return 0;
}
