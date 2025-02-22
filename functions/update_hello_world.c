// Elizabeth Gutierrez, Update Hello World C
#include <stdio.h>

void hello(char *name) {
    printf("Hello %s\n", name);
}

int main() {
    char name[100];

    printf("Give me a name: \n");
    scanf("%s", name);
    hello(name);

    printf("Give me another name: \n");
    scanf("%s", name);
    hello(name);

    printf("Give me another name: \n");
    scanf("%s", name);
    hello(name);

    printf("Give me another name: \n");
    scanf("%s", name);
    hello(name);

    printf("Give me one last name: \n");
    scanf("%s", name);
    hello(name);

    return 0;
}
