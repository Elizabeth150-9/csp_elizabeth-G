# Elizabeth Gutierrez, Financial Calculator python update
def info(cost, income, type):
    percent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")

def info()

# print statement that welcomes user and tells what the program does
print("Welcome to my financial calculator that will help you manage your monthly finances!:")
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
spending = income-rent-utilities-groceries-transportation-savings
# calculate percent income of rent (rent/income *100) (variable)
info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")