def find_even_number(num):
    for index in num:
        if index % 2 == 0:
            print("Even number: " + str(index))

find_even_number([10,20,2,3,4,5,9,10])