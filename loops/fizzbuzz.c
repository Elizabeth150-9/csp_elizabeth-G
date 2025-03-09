// Elizabeth Gutierrez, TEMPLATE
#include <stdio.h>

int main() {
    int x = 0;
    while (x < 51) {
        x = x + 1;
        if (x % 3 == 0 && x % 5 == 0) {
            printf("fizzbuzz\n");
        } else if (x % 3 == 0) {
            printf("fizz\n");
        } else if (x % 5 == 0) {
            printf("buzz\n");
        } else {
            printf("%d\n", x);
        }
    }
    return 0;
}

