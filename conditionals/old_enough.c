// Elizabeth Gutierrez, Old Enough in C
#include <stdio.h>
#include <string.h>

int main() {
    int age;
    printf("How old are you?:\n");
    scanf("%d", &age);

if(age == 18) {
    printf("You can vote!\n");
}

}else if(age > 16 || == 16){
     printf("You cannot drive.\n");
}else if(age < 15){
    printf("You cannot get your permit.\n");
}else{
    printf("You can get your permit!\n");
}

if(age == 4) {
    printf("You can go to school!\n");
}else if(age < 4){
    printf("You cannot go to school.\n");
}else{
    printf("You can go to school!\n");
}

    return 0;
}

