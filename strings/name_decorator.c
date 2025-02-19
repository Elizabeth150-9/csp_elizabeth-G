// Elizabeth Gutierrez, Name Decorator C
#include <stdio.h>

char subject[19];

int main(void){
    printf("Name:\n");
    scanf("%s", subject);
    char first[] = ":):):)";
    char second[] = "Elizabeth";
    char third[] = ":):):)";
    printf("%s", first);
    scanf(first, second);
     printf("%s", second);
     scanf(second, third);
     printf("%s", third);
    return 0;
}