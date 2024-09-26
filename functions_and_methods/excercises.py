# excercise 1 What happens when you run the following program? Why do we get that result?
'''
def set_foo():
    foo = 'bar'

set_foo()
print(foo)
'''
print('Excercise 1, It will cause an error when print(foo) runs because foo is only defined in the scope of the function')

print('-' * 45)

# excercise 2 What happens when you run the following program? Why do we get that result?

foo = 'bar'

def set_foo():
	foo = 'qux'

set_foo()
print(foo)

print('Excercise 2, It will print the global scope for foo which is bar.')

print('-' * 45)

# excercise 3 Write a program that uses a multiply function to multiply two numbers and returns the result.
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply(num1 , num2):
	return float(num1) * float(num2)

num1 = input('please enter a number: ')
num2 = input('please enter another number: ')

product = multiply(num1 , num2)
print(f'{num1} * {num2} = {product}')

print('-' * 45)

# excercise 4 identify items from code

print('function name = multiply_numbers - function arguments = 2, 3, 4 - function definiton = the first three lines of the code\
- function body = lines 2 and 3 - function parameters = num1, num2, num3 - function invocation = line 5 - function return value = num1 * num 2 * num3\
indentier = result')

print('-' * 45)

# excercise 5 what does the code print 

print('there is no print call so it doesn\'t print anything')
def scream(words):
    return words + '!!!!'

scream('Yipeee')

print('-' * 45)

# excercise 6 what does the code print 

print('the return is before print is called in the function so it doesn\'t print anything')

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

print('-' * 45)

# excercise 7 what does the code do

print('I think the code will print Hello and then an undefined error will occour because only 1 argument was passed so the second parameter has no value')

print('-' * 45)

# excercise 8 what does the code do

print('I think the code will print 42 and 3.141592 and ignore the 3rd argument that was passed because foo only excepts 2 parameters\
---- I was incorrect there was an error due to incorrect number of arguments being passed')

print('-' * 45)

# excercise 9 what does the code do

print('I think the code will print 42 and 3.141592 and 2.718. I think it will reassign the default values to the value of the arguments being passed')

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

print('-' * 45)

# excercise 10 what does the code do

print('I think the code will print 42 and 3.141592 and 2. I think it will reassign the default values to the value of the arguments being passed for second and third will keep the default value')

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

print('-' * 45)

print('-' * 45)

# excercise 11 what does the code do

print('I think the code will print 42 and 3 and 2.')

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

print('-' * 45)

# excercise 12 what does the code do

print('I think the code will give an error because no arguments are passed and first deos\'t have a default value.')

'''
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
'''

print('-' * 45)

# excercise 13 what does the code do

print('I think the code will give an error because no arguments are passed for third and it deos\'t have a default value.')

'''
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
'''

print('-' * 45)

# excercise 14 identify all identifiers

print('multiply - get_num - first_number - second_number - get_num - product - print.')

print('-' * 45)

# excercise 15 are identifiers global or local

print('multiply global - left local- right local - prompt local -  get_num global - first_number global - second_number global - get_num global - product global - print global.')

print('-' * 45)

# excercise 16 identify function names and parameters and line numbers 

print('function multiply lines 1 and 9 - parameter left lines 1 and 2 - parameter right lines 1 and 2 - parameter prompt lines 4 and 5 -  function get_num lines 4 7 and 8 - function print line 10.')

print('-' * 45)

# excercise 17 Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

print('function names are say(), print() input() and max() - print input and max are built in functions - the methods are .upper() and .lower() ')

print('-' * 45)

# excercise 18 use function to identify list not divisible by 3

def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

divisible1 = remainders_3(numbers_1)
divisible2 = remainders_3(numbers_2)
divisible3 = remainders_3(numbers_3)
divisible4 = remainders_3(numbers_4)

print(bool(divisible1))
print(bool(divisible2))
print(bool(divisible3))
print(bool(divisible4))

print('-' * 45)

# excercise 19 use function to identify list not divisible by 5

def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))