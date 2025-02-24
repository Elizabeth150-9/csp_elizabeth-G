// Elizabeth Gutierrez, Update Hello World C
#include <stdio.h>

void hello(char *name) {
    printf("Hello %s\n", name);
}

int main() {
    char name[50];
    char two[50];
    char three[50];
    char four[50];
    char five[50];

    printf("Give me a name: \n");
    scanf("%s", name);
    hello(name);

    printf("Give me another name: \n");
    scanf("%s", two);
    hello(two);

    printf("Give me another name: \n");
    scanf("%s", three);
    hello(three);

    printf("Give me another name: \n");
    scanf("%s", four);
    hello(four);

    printf("Give me one last name: \n");
    scanf("%s", five);
    hello(five);

    return 0;
}
