# Elizabeth Gutierrez, silly sentences python
 
#print("Welcome to my silly sentence in python program: ")

#name = (input("Enter a name: \n"))
#verb = (input("Enter a verb: \n"))
#noun = (input("Enter a noun: \n"))

#print(name, "likes to", verb, "with the", noun)




while True:    
    puzzle = input("To pick 1 a word scramble or riddle, insert 3 or 4.\n")    
    if puzzle == "3":   
        answer = input("imekilcr\n")   
        if answer.lower() == "limerick":
            print("You won black eyes!\n") 
            break  
        else:
            print("Incorrect, try again...\n")
    elif puzzle == "4":  
        answer = input("Maria has five children. Jack, Joane, Jonah, and Jane. What is the name of the fifth child?\n")    
        if answer.lower() == "what":    
            print("You won green eyes!\n")    
            break   
        else:    
            print("Incorrect, try again...\n")    
    else:  
        print("To pick 1 a word scramble or riddle, insert 3 or 4.\n")  

puzzles = ["Black eyes", "granny white hair", "big blue ball gown with elegant puffed sleeves", "purple heelys"]
for puzzle in puzzles:
    print("Your character has", puzzle)

prizes = ["Green eyes", "light up neon circus afro hair", "jean overalls with embroidered flowers on the pockets", "pink bedazzeled justice glow up sneakers"]
for prize in prizes:
    print("Your character has", prize)

wins = ["Black", "light up neon circus afro hair", "big blue ball gown with elegant puffed sleeves", "pink bedazzled justics glow up sneakers"]
for win in wins:
    print("Your character has", win)

selects = ["Green eyes", "granny white hair", "jean overalls with embroidered flowers on the pockets", "purple heelys"]
for select in selects:
    print("Your character has", select)