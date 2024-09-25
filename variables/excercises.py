# excercise 1 classify non-constant variable names
# index == idiomatic
# CatName == non-idiomatic  - Use snake_case formatting for these names
# lazy_dog == idiomatic
# quick_Fox == non-idiomatic - Use snake_case formatting for these names
# 1stCharacter == illegal - Starts with a digit
# oprand2 == idiomatic
# BIG_NUMBER == non-idiomatic - Use snake_case formatting for these names
# π == illegal - Names may only use letters and digits from the standard ASCII character set

# ------------------------------------------------------------

# excercise 2 classify function names
# index == idiomatic
# CatName == non-idiomatic - Use snake_case formatting for these names
# lazy_dog == idiomatic
# quick_Fox == non-idiomatic - Use snake_case formatting for these names
# 1stCharacter == illegal - Starts with a digit
# operand2 == idiomatic
# BIG_NUMBER == non-idiomatic - Use snake_case formatting for these names
# π == illegal - Names may only use letters and digits from the standard ASCII character set

# ------------------------------------------------------------

# excercise 3 classify constant names
# index == non-idiomatic - Use SCREAMING_SNAKE_CASE formatting for these names.
# CatName == non-idiomatic - Use SCREAMING_SNAKE_CASE formatting for these names.
# snake_case == non-idiomatic - Use SCREAMING_SNAKE_CASE formatting for these names.
# LAZY_DOG3 == idiomatic
# 1ST == illegal - Starts with a digit
# operand2 == non-idiomatic - Use SCREAMING_SNAKE_CASE formatting for these names.
# BIG_NUMBER == idiomatic 
# Π == illegal - Names may only use letters and digits from the standard ASCII character set

# ------------------------------------------------------------

# excercise 4 classify class names
# index == non-idiomatic - Use PascalCase formatting for these names. PascalCase is sometimes called CamelCase (with both Cs capitalized
# CatName == idiomatic
# Lazy_Dog == non-idiomatic - Use PascalCase formatting for these names. PascalCase is sometimes called CamelCase (with both Cs capitalized
# 1ST == illegal - Starts with a digit
# operand2 == non-idiomatic - Use PascalCase formatting for these names. PascalCase is sometimes called CamelCase (with both Cs capitalized
# BigNumber3 == idiomatic 
# Πi == illegal - Names may only use letters and digits from the standard ASCII character set

# ------------------------------------------------------------

print('answers to excercises 1-4 in comments')

print('-' * 45)

# excercise 5 write a program that uses a variable in 3 different greetings 
print('excercise 5')
name  = 'Brett'
print('Good Morning,' , name)
print('Good Afternoon,' , name)
print('Good Evening,' , name)

print('-' * 45)

# excercise 6 write program that takes age variable and calculates age for 10, 20 ,30 and 40 years from now
print('excercise 6')
age = 42
years_in_10 = 10
years_in_20 = 20
years_in_30 = 30
years_in_40 = 40 
print('You are' , age , 'years old.')
print('In' , years_in_10 , 'years, you will be' , age + years_in_10 , 'years old.')
print('In' , years_in_20 , 'years, you will be' , age + years_in_20 , 'years old.')
print('In' , years_in_30 , 'years, you will be' , age + years_in_30 , 'years old.')
print('In' , years_in_40 , 'years, you will be' , age + years_in_40 , 'years old.')

print('-' * 45)

# excercise 7 what happens when you run the following code? why?
print('excercise 7, the code will greet Victor 3 times and then Nina 3 times. Constant variables can be changed but they should\'t.\
 If the NAME variable is intended to change it should be named "name"')
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

print('-' * 45)

# excercise 8 create programm to track bank balance with compound interest
balance = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print('excercise 8, the balance after 5 years would be' , balance)

print('-' * 45)

# excercise 9 create programm to track bank balance with compound interest displayed one year at a time with augmented assignment
print('excercise 9')
balance = 1000.00
balance *= 1.05
print('After 1 year balance would be' , balance)
balance *= 1.05
print('After 2 years balance would be' , balance)
balance *= 1.05
print('After 3 years balance would be' , balance)
balance *= 1.05
print('After 4 years balance would be' , balance)
balance *= 1.05
print('After 5 years balance would be' , balance)

# excercise 10 is the variable reassigned, mutated or neither
# obj = 'ABcd' -- reassign
# obj.upper()  -- neither
# obj = obj.lower() -- reassign
# print(len(obj)) -- neither
# obj = list(obj) -- reassign
# obj.pop()  -- mutate
# obj[2] = 'X' -- mutate
# obj.sort() -- mutate
# set(obj) -- neither
# obj = tuple(obj) -- reassign