def print_hi(name):
    print(f'Welcome to the python world, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def find_even_number(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)



if __name__ == '__main__':
    print_hi('Maha')
    find_even_number([1,3,4,6,90,7,34])
