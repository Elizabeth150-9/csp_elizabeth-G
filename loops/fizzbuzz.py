# Elizabeth Gutierrez, FizzBuzz in Python
x = 0
nums = int(input("Choose Number: "))
while x <= nums:
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
    x+= 1