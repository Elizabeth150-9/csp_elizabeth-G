# Elizabeth Gutierrez, Financial Calculator python

# print statement that welcomes user and tells what the program does
subject = input("Welcome to my program:")
# ask what their income is (variable an input)
income = float(input("What is your income\n"))
# ask what their rent is (variable an input)
rent = float(input("How much is your rent\n"))
# ask what their utilities is (variable an input)
utilities = float(input("What are your utilities\n"))
# ask what their groceries is (variable an input)
groceries = float(input("How much are your groceries\n"))
# ask what their transportation is (variable an input)
transportation = float(input("How much is your transportation\n"))
# calculate savings as 10% of income (income*.1) (variable)
savings = float(input("What are your savings\n"))
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = float(input("What are your spendings\n"))
# calculate percent income of rent (rent/income *100) (variable)
l = rent/income *100
# calculate percent income of utilities (utilities/income *100) (variable)
p = utilities/income *100
# calculate percent income of groceries (groceries/income *100) (variable)
r = groceries/income *100
# calculate percent income of transportation (transportation/income *100) (variable)
c = transportation/income *100
# calculate percent income of spending (spending/income *100) (variable)
# Your rent is $XX.XX which is XX% of your income. (Print)
Print()
# Your utilities is $XX.XX which is XX% of your income. (Print)
Print()
# Your groceries is $XX.XX which is XX% of your income. (Print)
Print()
# Your transportation is $XX.XX which is XX% of your income. (Print)
Print()
# Your savings is $XX.XX which is XX% of your income. (Print)
Print()
# Your spending is $XX.XX which is XX% of your income. (Print)
Print()