# Elizabeth Gutierrez, Old Enough in Python
age = int(input("How old are you?:\n"))
if age >= 18:
    print("You can vote!")
elif age >= 16:
    print("You can drive!")
elif age >= 15:
    print("You can get your permit!")
elif age >= 6:
    print("You can go to school!")
else:
    print("You cannot go to school")
