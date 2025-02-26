# Elizabeth Gutierrez, Conditionals notes Python
name = input("What is your name?:\n")
#1. What puts something inside of the “if” statement?
# Having a tab/white space makes something inside of an if statement.
<<<<<<< HEAD
if name == "LaRose":
    print("Hi Ms. LaRose")
else: # happens if condition is false.
    print(f"Hello {name}!")

=======
if name == "Elizabeth":
    print("Elizabeth")
else: 
        print(f"Hello {name}!")
#happens if condition is false.
>>>>>>> 0d9360a0195fbc64745ea54fe853d60317c88bf0
#2. What do if statements do?
# if statements checks a condition and it it is true, it will do a thing.
if name == "Ms. LaRose": # <= this is the condition.
    print("Hi Mr. LaRose") # <= What it does if true.

#3. What are boolean statements? 
# A boolean statement is the part of conditional that is either true or false(true or false statement).
<<<<<<< HEAD
if name == "LaRose": # <- This is the boolean statement(either true or false).
    print("Hi Ms. LaRose")
else: # happens if condition os false.
    print(f"Hello {name}!")
=======
if name == "Elizabeth": # <- This is the boolean statement(either true or false).
    print("Elizabeth")
else: 
        print(f"Hello {name}!")
>>>>>>> 0d9360a0195fbc64745ea54fe853d60317c88bf0

#4. What do else statements do?
if name == "LaRose":
    print("Hi Ms. LaRose")
else: #if boolean is false, the else statement happens.
    print(f"Hello {name}!")
# else statements shows if boolean statement is false.

#5. What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("How many cookies are there?\n"))
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
<<<<<<< HEAD
if num < 10 and num > 5: #And both booleans must be true.
      print("This is a big single digit number")
elif num < 10 or num > 5: #or means one must be true.
      print("This is a big single digit number")
elif not num < 10: #Not changes it to check if false.
      print("This is a big single digit number")
=======
elif num < 10 and num > 5: #And both booleans must be true.
    print("This is a big single digit number")

elif num < 10 or num > 5: #or means one must be true.
    print("This is a big single digit number")

elif not num < 10: #Not changes it to check if false.
    print("This is not a single digit number")
>>>>>>> 0d9360a0195fbc64745ea54fe853d60317c88bf0

#8. What are logical operators for?
#Allows the code to handle more difficult question, increases complexity.

#9. What does a nested conditional statement do?
if num < 10:
    if num ==8:
        print("This prints at 8")
    else:
        if num == 4:
<<<<<<< HEAD
            print("There are only enough cookies left for me")
        else:
            print("The number is less than 10")
=======
            print("There are only enough cookies left for me. . . sorry")
        else:
        print("The number is less than 10")
>>>>>>> 0d9360a0195fbc64745ea54fe853d60317c88bf0
else:
    print("The number is bigger than 10")

# you can nest as many conditionals as you want, but stop at three to not confuse it.