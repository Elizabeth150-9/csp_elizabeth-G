// Elizabeth Gutierrez, Name Decorator C
#include <stdio.h>
#include <string.h>

char name[19];

int main(void){
    printf("Your name:\n");
    scanf("%s", name);
    char a[] = ":):):)";
    char b[] = "Elizabeth";
    char c[] = ":):):)";
    printf("%s", a);
    strcat(a, b);
     printf("%s", b);
     strcat(b, c);
     printf("%s", c);
    return 0;
}