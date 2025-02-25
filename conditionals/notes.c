// Elizabeth Gutierre, Conditionals notes C
#include <stdio.h>
#include <string.h> //needed to compare strings
char name[]= "Elizabeth";
int num;

int main(void){
    //10. How do you write an if statement in C?
    if(strcmp(name, "Elizabeth") == 0){ //strcmp measn string comparison when the outcome is 0 the string are the same.

        printf("Hello Elizabeth, welcome to my class.\n");
    //11. How do you write an else statement in C?
    }else{
        printf("Hello %s, welcome to my class.\n", name);
    }
    printf("How many siblings do you have?\n"); //for practice assignment
    scanf("%d", &num);
    //12. How do you write elif/ else if statements in C?
    if(num == 0){
    printf("You are an only child\n");
    }else if(num <= 2){
        printf("You have a couple siblings\n");
    }else if(num <= 5){
        printf("You have a few siblings\n");
    }else{
        printf("Your have a lot of sbilings\n");
    }

   //13. How do you write the 3 logical operators in C?
   // && = and
   // || = or
   // ! = not

   if(num == 7 ||  num == 13){
      printf("%d is an unlucky number\n", num);
    }else if (num <10 && num <5){
      printf("%d is a large single digit number\n", num);
   }else if(!(num > 10)){
       if(num == 12){
           printf("That is a dozen!\n");
       }else{
           printf("%d is a big number\n", num);
       }
   }else{
      printf("You typed in %d\n", num);
   }
   return 0;
}
