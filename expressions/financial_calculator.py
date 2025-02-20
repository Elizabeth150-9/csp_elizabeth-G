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
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
savings = income*.1
spending = float(income-rent-utilities-groceries-transportation-savings)
# calculate percent income of rent (rent/income *100) (variable)
percent_rent = rent/income *100
# calculate percent income of utilities (utilities/income *100) (variable)
percent_utilities = utilities/income *100
# calculate percent income of groceries (groceries/income *100) (variable)
percent_groceries = groceries/income *100
# calculate percent income of transportation (transportation/income *100) (variable)
percent_transportation = transportation/income *100
# calculate percent income of spending (spending/income *100) (variable)
percent_spending = spending/income *100
# calculate 
percent_savings = 10%income
# Your rent is $XX.XX which is XX% of your income. (Print)
print(f"Your rent costs {rent} which is {percent_rent: .2f} % of your income.\n")
# Your utilities is $XX.XX which is XX% of your income. (Print)
print(f"Your utilities cost {utilities} which is {percent_utilities: .2f} % of your income:\n")
# Your groceries is $XX.XX which is XX% of your income. (Print)
print(f"Your groceries cost {groceries} which is {percent_groceries: .2f} % of your income:\n")
# Your transportation is $XX.XX which is XX% of your income. (Print)
print(f"Your transportation costs {transportation} which is {percent_transportation: .2f} % of your income:\n")
# Your savings are $XX.XX which is XX% of your income. (Print)
print(f"Your savings are {savings} which is {percent_savings: .2f} % of your income:\n")
# Your spending is $XX.XX which is XX% of your income. (Print)
print(f"Your money leftover is {spending} which is {percent_spending: .2f} % of your income:\n")
