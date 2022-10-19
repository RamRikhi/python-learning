from datetime import datetime
import sys

# Author:  Rikhi
# Date: 05/09/2022
# Copyright @ 2022

# This function will take name as input and based on current system time it will greet the user
def greet_user(name):
    date = datetime.now().hour
    if date < 12:
            print("Good Morning " + name)
    elif date < 17:
            print("Good Afternoon " + name)
    elif date < 23:
            print("Good Evening " + name)
    else:
            print("Good Night " + name)


# Calling greet_user() function
greet_user(sys.argv[1] + " " + sys.argv[2])