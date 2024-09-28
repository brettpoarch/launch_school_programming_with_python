import math 

def page_break():
	print('-' * 45)

# excercise 1 What does the following function do? Be sure to identify the output value.

print('the function will sort the dict by keys and make the second key uppercase')

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

page_break()

print(math.sqrt(37))

def square_root(num):
     return math.sqrt(num)

print(square_root(37))
     

page_break()

def sum_of_squares(num1, num2):
    def square(num):
         return num * num
    
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

page_break()

def increment_counter():
    global counter
    counter += 1
    return counter

counter = 0

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

page_break()

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()