# Elizabeth Gutierrez, Old Enough in Python
age = int(input("How old are you?:\n"))
if age > 18:
    print("You can vote!")
elif age < 18 or age == 18:
    print("You cannot vote.")

if age > 16:
    print("You can drive!")
elif age < 16 or age == 16:
    print("You cannot drive.")

if age > 15:
    print("You can get your permit!")
elif age < 15 or age == 15:
    print("You cannot get your permit.")

if age > 4:
    print("You can go to school!")
elif age < 4 or age == 4:
    print("You cannot go to school.")