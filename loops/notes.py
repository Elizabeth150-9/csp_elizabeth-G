# Elizabeth Gutierrez, Loops Notes in Python

# 1.What is a loop? 
    #section of code that repeats multiple times
# 2.What are the two types of loops?
    #for loop
nums = [12,3,66,7,3,3,2]

for num in nums:
    print(num)

    #while loop
x = 0

while x < 10:
    print(x)
    x+= 1
# 3.What is iteration
    #That particular/specific instance of the loop
    #iteration is the amount of times you are looping through(Looping over and using it many times)

# 4.What are lists? 
# variable that holds multiple values
nums = [1,2,3,4,5,6,7,6]
siblings = ["Alex", "Kate", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Hailey"]
print(nums) #prints whole list(UGLY\dont)
print(siblings[3]) #prints 1 item from the list(Starts counting at 0)

siblings[7] = "Jake"
siblings.pop(5) #removes item
siblings.insert(1, "Jayshree") #adds item
siblings.insert(2, ["Joe", "Noah", "Zee"])
print(siblings)


#5. How do you make lists in python? 
    #1st, Brackets. 2nd, add items with correct data types. 3rd, comma between each item.

#6. How do you make for loops in python? (Use plural words)
for sibling in siblings:
    print(sibling) 

for x in range(0,101, 20):
    print(x)

#7. How do you make while loops in python?
import random 
x = 1#variable to keep count of iteration
goose = random.randint(1,20)

while x <= 20:
    if x == goose:
        print("Goose!")
        break #tells loop to stop
    else:
        print("Duck")
    x+= 1