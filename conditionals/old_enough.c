// Elizabeth Gutierrez, Old Enough in C
#include <stdio.h>
#include <string.h>

char vote[] = "vote";
char drive[] = "drive";
char permit[] = "permit";
char school[] = "school";

int main() {
    int vote;
    printf("How old are you?:\n");
    scanf("%d", &vote);
    if (vote >= 18) {
        printf("You can vote!\n");
    }else{
        printf("You cannot vote.\n");
    }

    int drive;
    printf("How old are you?:\n");
    scanf("%d", &drive);
    if (drive >= 16) {
        printf("You can drive!\n");
    }else{
        printf("You cannot drive.\n");
    }

    int learners_permit;
    printf("How old are you?:\n");
    scanf("%d", &learners_permit);
    if (learners_permit >= 15) {
        printf("You can get your learners permit!\n");
    }else{
        printf("You cannot get your learners permit.\n");
    }

    int school;
    printf("How old are you?:\n");
    scanf("%d", &school);
    if (school >= 4) {
        printf("You can go to school!\n");
    }else{
        printf("You cannot go to school.\n");
    }

    return 0;
}