# Elizabeth Gutierrez, Time of day in Python

import time

num1 = "Goodmorning"
num2 = "Good afternoon"
num3 = "Good evening"
i=int(time.time())+60  # setting a checkpoint 60s in the future
if num1 < num2:
    print("Good morning!")
    print("Good afternoon!")
    print("Good evening!")
    
def time_to_min(hour, minute):
    return hour*60+minute

timenow = time.localtime()

morning = timenow.tm_hour
afternoon = timenow.tm_hour
evening = timenow.tm_hour

if evening >= morning and evening <= afternoon:
    print("Good morning!\n")
elif:
    print("Good morning!\n") 
