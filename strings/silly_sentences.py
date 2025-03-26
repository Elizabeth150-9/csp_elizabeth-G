# Elizabeth Gutierrez, silly sentences python
 
#print("Welcome to my silly sentence in python program: ")

#name = (input("Enter a name: \n"))
#verb = (input("Enter a verb: \n"))
#noun = (input("Enter a noun: \n"))

#print(name, "likes to", verb, "with the", noun)



#puzzle = input("To pick 1, a word scramble or riddle,  insert 3 or 4.\n")
#third = ("Limerick")
#fourth = ("What")
#option_3 = input("")
#option_4 = input("")
#if option_3 == 3:
#    print("imklerci\n")
#elif option_3 == "Limerick":
#    print("Correct, you won black eyes!\n")
#else:
#    print("Incorrect, try again.\n")
#if option_4 == 4:
#    print("Maria has five children. Jack, Jacob, Joane, and Jane. What is the name of the fifth child?\n")
#elif option_4 == "What":
#    print("Correct, you won green eyes!\n")
#else:
#    print("Incorrect, try again.\n")




while True:    
    puzzle = input("To pick 1 a word scramble or riddle, insert 3 or 4.\n")    
    if puzzle == "3":   
        answer = input("imekilcr\n")   
        if answer.lower() == "limerick":
            print("Correct, you won black eyes!\n") 
            break  
        else:
            print("Incorrect, try again...\n")
    elif puzzle == "4":  
        answer = input("Maria has five children. Jack, Joane, Jonah, and Jane. What is the name of the fifth child?\n")    
        if answer.lower() == "what":    
            print("Correct, you won green eyes!\n")    
            break   
        else:    
            print("Incorrect, try again...\n")    
    else:  
        print("To pick 1 a word scramble or riddle, insert 3 or 4.\n")  



