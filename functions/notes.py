# Elizabeth Gutierrez, Functions Notes Python

#functions hold actions to be reused
#number = int(input("Please tell me a number:\n"))
def add(numOne, numTwo):#parameters set the name of the variable
    #print(numOne+numTwo)
    return numOne+ numTwo
    
#add(number,21)#arguments set the value of the variable
#print(add(8,12))
#addition = add(8,12)
#print(add(addition,4))
#add(87,3)

def values(type):
    return input(f"Please give me a {type}:\n")

name = values("name")
place = values("place")
verb = values("verb (past tense)")

print(f"{name} was really fast getting to {place} because they {verb}ed the whole way there.")




#numOne = int(input("Please tell me a number:\n"))
    #numTwo = int(input("Please tell me another number:\n"))
    #print(numOne+numTwo)
