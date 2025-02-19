// Elizabeth Gutierrez, Financial Calculator C
#include <stdio.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;
float spendings;

int main(void){
   printf("Welcome to my financial calculator in c program! \n");
   printf("How much is your monthly income: \n");
   scanf("%f", &income);
   printf("How much is your monthly rent?\n");
   scanf("%f", &rent);
   printf("How much are your utilities monthly?\n");
   scanf("%f", &utilities);
   printf("How much are you groceries monthly?\n");
   scanf("%f", &groceries);
   printf("How much is your transportation?\n");
   scanf("%f", &transportation);
   float savings = income*.1;
   float spendings = income-savings-rent-utilities-groceries-transportation;
   float percent_rent = rent/income *100;
   float percent_utilities = utilities/income *100;
   float percent_groceries = groceries/income *100;
   float percent_transportation = transportation/income *100;
   float percent_spendings = spendings/income *100;
   float percent_savings = savings/income *100;
   printf("Your rent costs %.2f which is %.2f percent of your income\n", rent, percent_rent);
   printf("Your utilities cost %.2f which is %.2f percent of your income\n", utilities, percent_utilities);
   printf("Your groceries cost %.2f which is %.2f percent of your income\n", groceries, percent_groceries);
   printf("Your transportation costs %.2f which is %.2f percent of your income\n", transportation, percent_transportation);
   printf("Your savings are %.2f which is %.2f percent of your income\n", savings, percent_savings);
   printf("Your money left to spend is %.2f which is %.2f percent of your income\n", spendings, percent_spendings);
  return 0;
}