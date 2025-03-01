# Elizabeth Gutierrez, Time of day in Python

import datetime

currenttime = datetime.datetime.now()

print(currenttime.hour)

if currenttime.hour <= 12:
    print("Good morning!")
elif currenttime.hour <= 18:
    print("Good afternoon!")
else:
    print("Good evening!")

