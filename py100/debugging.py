def page_break():
	print('-' * 45)

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among([0, 0, 1, 0, 2, 0])
find_first_nonzero_among([1])

print('The first time we call the function we get the TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given \n\
      the argument on function only excepts one parameter but we are passing 6 individual arguments. In the second call we get the TypeError: \'int\' object is not iterable \n\
      in the function we\'re asking the program to iterate through a collection but we\'re not passing a collection in the argument. in both cases we can make the\n\
      argument a collection likea list and the program will run ')

page_break()

import random

def predict_weather():
    sunshine = random.choice([True, False])
    
    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

print('the program was assigning a str value to sunshine. as long as the string isn\'t empt it\'ll evasluate as True. we need to set sunshone to the bool values of True or False')

def multiply_by_five(n):
    return int(n) * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")

print('The function is receiveing the argument as a str. we need to change the parameter to a int before we return the value')

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

page_break()

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

print('We werent returning anything after running the function')

page_break()

numbers = []

for i in range(5):
    numbers.append(i + 1)

print(numbers)

page_break()

info = {'name': 'Srdjan', 'age': 38}

print(info.get('city'))

page_break()

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = 'X'
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

print('all the nested lists are the same object. we need to create a copy')

page_break()

def find_maximum(numbers):
    if not numbers:
        return None
    
    max_number = numbers[0]
    
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

print('We have max number intitialized at 0 I changed that to numbers[0] for cases where all numbers in the list are negative ')

page_break()

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1
  
    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0

print('we initialized product with 0 resulting in all multuplications of 0. I intialized product with 1')