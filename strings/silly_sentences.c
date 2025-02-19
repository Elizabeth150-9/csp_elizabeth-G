// Elizabeth Gutierrez, silly sentences C
#include <stdio.h>
#include <string.h>

char name[50];
char verb[50];
char noun[50];

int main(){
    printf("Welcome to my silly sentences program in C! \n");
    printf("Enter a name: \n");
    scanf("%s", name);

    printf("Enter a verb: \n");
    scanf("%s", verb);

    printf("Enter a noun: \n");
    scanf("%s", noun);

printf("%s likes to %s with my %s", name, verb, noun);
   return 0;
   }