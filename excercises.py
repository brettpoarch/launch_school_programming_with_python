def page_break():
	print('-' * 45)

# excercise 1 The following code causes an infinite loop (a loop that never stops iterating). Why?

print('The counter is initialized at 0 and the loop is set to run while counter is < 5. counter is never increased so the loop will run forever ')

page_break()

# excercise 2 Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.

age = input('How old are you?\n')

'''
print(f'You are {age} years old.')
print(f'In 10 years, you will be {int(age) + 10} years old.')
print(f'In 20 years, you will be {int(age) + 20} years old.')
print(f'In 30 years, you will be {int(age) + 30} years old.')
print(f'In 40 years, you will be {int(age) + 40} years old.')
'''
print(f'You are {age} years old.')

for number in range(10, 50, 10):
	print(f'In {number} years, you will be {int(age) + number} years old.')

page_break()

# excercise 3 Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list):
	print(my_list[index])
	index += 1

for member in my_list:
	print(member)

page_break()

# excercise 4 Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list):

	if my_list[index] % 2 == 0:
		print(my_list[index])

	index += 1

for member in my_list:
	if member % 2 != 0:
		print(member)

page_break()

# excercise 5 Print all of the even numbers in the following list of nested lists. Don't use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
	for number in list:
		if number % 2 == 0:
			print(number) 

page_break()

# excercise 6 Let's try another variation on the even/odd-numbers theme.

new_list = []

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

for number in my_list:
	if number % 2 == 0:
		new_list.append('even')
	else:
		new_list.append('odd')

print(new_list)

page_break()

# excercise 7 Write a find_integers function that returns a list of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(tuple):
	found_ints = []
	for member in tuple:
		if type(member) == int:
			found_ints.append(member)

	return found_ints

integers = find_integers(my_tuple)
print(integers)                   

page_break()

# excercise 8 Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key.
# Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

name_length = { name : len(name) 
			   for name in my_set 
			   if len(name) % 2 != 0 }

print(name_length)

page_break()

# excercise 9 Write a function that computes and returns the factorial of a number by using a for or while loop. 
# The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

def factorial(num):

	result = 1

	for num in range(1, num + 1):
		result *= num

	return result

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000


page_break()

# excercise 11 Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
counter = 0
ii = 0

while index < len(my_list):
	while counter < len(my_list[ii]):
		if my_list[ii][counter] % 2 == 0:
			print(my_list[ii][counter])
		counter += 1
	
	index += 1
	ii += 1
	counter = 0


