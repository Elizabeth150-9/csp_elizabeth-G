# Elizabeth Gutierrez, Old Enough in Python
vote = int(input("How old are you?:\n"))
if vote >= 18:
    print("You can vote!")
elif vote <= 18:
    print("You cannot vote.")
else:
    print(f"You {vote}.")

drive = int(input("How old are you?:\n"))
if drive >= 16:
    print("You can drive!\n")
elif drive <= 16:
    print("You cannot drive.\n")
else:
    print(f"You {drive}.")

permit = int(input("How old are you?:\n"))
if permit >= 15:
    print("You can get your learners permit!\n")
elif permit <= 15:
    print("You cannot get your learners permit.\n")
else:
    print(f"You {permit}.")

school = int(input("How old are you?:\n"))
if school >= 4:
    print("You can go to school!\n")
elif school <= 4:
    print("You cannot go to school.\n")
else:
    print(f"You {school}.")