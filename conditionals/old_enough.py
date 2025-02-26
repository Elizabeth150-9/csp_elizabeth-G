# Elizabeth Gutierrez, Old Enough in Python
vote = int(input("How old are you?:\n"))
if vote > 18:
    print("You can vote!")
elif vote < 18:
    print("You cannot vote.")

drive = int(input("How old are you?:\n"))
if drive > 16:
    print("You can drive!")
elif drive < 16:
    print("You cannot drive.")

learners_permit = int(input("How old are you?:\n"))
if learners_permit > 15:
    print("You can get your learners permit!")
elif learners_permit < 15:
    print("You cannot get your learners permit.")

school = int(input("How old are you?:\n"))
if school > 4:
    print("You can go to school!")
elif school < 4:
    print("You cannot go to school.")