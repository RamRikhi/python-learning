from datetime import datetime

def send_greeting(name):
    current_time =  datetime.now().hour
    if current_time <= 12:
        print("Good morning " + name)
    elif current_time <= 16:
        print("Good afternoon " + name)
    elif current_time <= 23:
        print("Good evening " + name)
    else:
        print("Good night " + name)

def find_even_number(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)



if __name__ == '__main__':
<<<<<<< HEAD
    print_hi('Maha')
    find_even_number([1,3,4,6,90,7,34])
=======
    send_greeting('Maha')

>>>>>>> f19af1b2797e49ab81f59836f155fada2e19f948
