// Elizabeth Gutierrez, My Family Loops in C
#include <stdio.h>

int main(){
    const char *names[] = {"Saul", "Ingrid", "Rebeca", "Betel", "Ema", "Saul"};
    int size = sizeof(names)/sizeof(names[0]);
    
    for (int m=0;m<size;m++) {
        printf("Hello %s, The sky is blue!\n", names[m]);
    }
    
    return 0;
}
