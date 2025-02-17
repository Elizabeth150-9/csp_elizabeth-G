// Elizabeth Gutierrez, Financial Calculator C
#include <stdio.h>

char welcome[19];
char income[50];
char rent[50];
char utilities[50];
char groceries[50];
char transportation[50];
char savings[50];
char spendings[50];

int main(void){
   printf("Welcome to my program.\n");
   scanf("%s", income);
   
   printf("How much is your income?\n");
   scanf("%s", income);
 
   printf("How much is your rent?\n");
   scanf("%s", rent);

   printf("How much are your utilities?\n");
   scanf("%s", utilities);

   printf("How much are you groceries?\n");
   scanf("%s", groceries);

   printf("How much is your transportation?\n");
   scanf("%s", transportation);

   printf("How much are your savings?\n");
   scanf("%s", savings);

   printf("How much are your spendings?\n");
   scanf("%s", spendings);

   int rent = (rent/income *100);

   int utilities = (utilities/income *100);

   int groceries = (groceries/income *100);

   int transportation = (transportation/income *100);

   int spendings = (spendings/income *100);

   int savings = (savings/income *100);

// Your rent is $XX.XX which is XX% of your income. (Print)
   printf("Your rent costs", "%s", rent, "which is", int rent, "% of your income:\n");
// Your utilities is $XX.XX which is XX% of your income. (Print)
   printf("Your utilities cost", "%s", utilities, "which is", int utilities, "% of your income:\n");
// Your groceries is $XX.XX which is XX% of your income. (Print)
   printf("Your groceries cost", "%s", groceries, "which is", int groceries, "% of your income:\n");
// Your transportation is $XX.XX which is XX% of your income. (Print)
   printf("Your transportation costs", "%s", transportation, "which is", int transportation, "% of your income:\n");
// Your savings is $XX.XX which is XX% of your income. (Print)
   printf("Your savings are", "%s", savings, "which is", int savings, "% of your income:\n");
// Your spending is $XX.XX which is XX% of your income. (Print)
   printf("Your spendings cost", "%s", spendings, "which is", int spendings, "% of your income:\n")
  return 0;
}