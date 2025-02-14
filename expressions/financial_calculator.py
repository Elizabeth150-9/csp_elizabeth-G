# Elizabeth Gutierrez, Financial Calculator python



# print statement that welcomes user and tells what the program does
subject = input("Welcome to my program:")
# ask what their income is (variable an input)
income = float(input("What is your income\n"))
# ask what their rent is (variable an input)
rent = float(input("How much is your rent\n"))
# ask what their utilities is (variable an input)
utilities = float(input("How much are your utilities\n"))
# ask what their groceries is (variable an input)
groceries = float(input("How much are your groceries\n"))
# ask what their transportation is (variable an input)
transportation = float(input("How much is your transportation\n"))
# calculate savings as 10% of income (income*.1) (variable)
savings = float(input("What are your savings\n"))
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = float(input("What are your spendings\n"))
# calculate percent income of rent (rent/income *100) (variable)
percent_rent = rent/income *100
# calculate percent income of utilities (utilities/income *100) (variable)
percent_utilities = utilities/income *100
# calculate percent income of groceries (groceries/income *100) (variable)
percent_groceries = groceries/income *100
# calculate percent income of transportation (transportation/income *100) (variable)
percent_transportation = transportation/income *100
# calculate percent of savings (savings/income *100) (variable)
percent_savings = savings/income *100
# calculate percent income of spending (spending/income *100) (variable)
percent_spending = spending/income *100
# Your rent is $XX.XX which is XX% of your income. (Print)
print = input("Your rent costs", percent_rent, "which is", percent_utilities, "% of your income:\n")
# Your utilities is $XX.XX which is XX% of your income. (Print)
print = input("Your utilities cost", percent_utilities, "which is", percent_utilities, "% of your income:\n")
# Your groceries is $XX.XX which is XX% of your income. (Print)
print = input("Your groceries cost", percent_groceries, "which is", percent_groceries, "% of your income:\n")
# Your transportation is $XX.XX which is XX% of your income. (Print)
print = input("Your transportation costs", transportation, "which is", percent_transportation, "% of your income:\n")
# Your savings is $XX.XX which is XX% of your income. (Print)
print = input("Your savings cost", savings, "which is", percent_savings, "% of your income:\n")
# Your spending is $XX.XX which is XX% of your income. (Print)
print = input("Your spendings cost", spending, "which is", percent_spending, "% of your income:\n")