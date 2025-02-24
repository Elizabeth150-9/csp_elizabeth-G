# Elizabeth Gutierrez, Conditionals notes Python
name = input("What is your name?:\n")
#1. What puts something inside of the “if” statement?
# Having a tab/white space makes something inside of an if statement.
if name == "Elizabeth":
    print("Elizabeth")
    else: #happens if condition is false.
        print(f"Hello {name}!")

#2. What do if statements do?
# if statements checks a condition and it it is true, it will do a thing.
if name == "Elizabeth": # <- this is the condition.
    print("Elizabeth") # <- What it does if true.

#3. What are boolean statements? 
# A boolean statement is the part of conditional that is either true or false(true or false statement).
if name == "Elizabeth": # <- This is the boolean statement(either true or false).
    print("Elizabeth")
    else: 
        print(f"Hello {name}!")

#4. What do else statements do?
if name == "Elizabeth":
    print("Elizabeth")
else: #if boolean is false, the else statement happens.
        print(f"Hello {name}!")
# else statements shows if boolean statement is false.

#5. What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("How many cookies are there"))
#computers read top to bottom, check the leat likely first(more specific on top, less specific on bottom).
if num == 0: # <- if always starts the conditional
    print("There are none.")
elif num == 1: # <- everything in between should be elif.
    print("There is one.")
elif num <4: # <- everything in between should be elif.
    print("There are a couple")
elif num < 10: # <- everything in between should be elif.
    print("There are a few")
else: # <- always ends the conditional
    print("There are many")
#6. What do each of the different symbols mean in conditionals?
#< This means less than
#> This means greater than
#<= This means less than or equal to
#>= This means greater than or equal to
#== This means equal to
#=== Doesn't exist in python(only in C)
#! This means not
#7. What are the 3 logical operators?
elif num <10 and num > 5: #And both booleans must be true.
    print("This is a big single digit number")

elif num <10 or num > 5: #or means one must be true.
    print("This is a big single digit number")

elif not num < 10: #Not changes it to check if false.
    print("This is a big single digit number")

#8. What are logical operators for?
#Allows the code to handle more difficult question, increases complexity.

#9. What does a nested conditional statement do?
if num <10:
    if num ==8:
        print("This prints at 8")
    else:
        print("The number is less thatn 10")
else:
    print("The number is bigger than 10")

#10. How do you write an if statement in C?
#11. How do you write else statements in C?
#12. How do you write elif/ else if statements in C?
#13. How do you write the 3 logical operators in C?