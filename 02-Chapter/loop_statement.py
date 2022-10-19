
# Author: Rikhi
# Date: 09/09/2022
# Copyright @ 2022

#This fucntion is able to filter even numbers

def find_even_number(num):
    for index in num:
        if index % 2 == 0:
            print("Even number: " + str(index) * 2)

find_even_number([10,20,2,3,4,5,9,10])