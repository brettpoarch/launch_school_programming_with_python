def page_break():
	print('-' * 45)

print('Question 1 because True is true the statement will run and set the variable my_value to 20.\n\
If we run the code with the False value we\'ll get an error because the variable my_new_value hasn\'t been intialized')

if True:
    my_value = 20

print(my_value)

#if False:
#    my_new_value = 42

#print(my_new_value)

page_break()

print('Question 2 my_function will pint 15. since x isn\'t definied as a local variable the program will use the global variable x - this is incorrect the function can access the global variable but no\n\
reassign it without the global keyword')

x = 10

def my_function():
   # x = x + 5
    print(x)

my_function()

page_break()

print('Question 3 my_function will print 1. a is initialized in the function and the conditional is True which will result in print(a)')

def my_function():
    a = 1

    if True:
        print(a)

my_function()

page_break()

print('Question 4 my_function will print 1. since a is not intialized locally the function will look to see if there\'s a global variable a')

a = 1

def my_function():
    print(a)

my_function()

page_break()

print('Question 5 my_function will print 1. the local variable a wasn\'t initialized until after the print statement ran  - this is incorrect my_function returned an error\n\
because there is a local a variable but it wasn\'t initialized until after the print statement')

a = 1

def my_function():
    a = 2
    print(a)
    #a = 2

my_function()

page_break()

print('Question 6 this will print the global variable 1. global variable won\'t be reassigned unless we use the global keyword ')

a = 1

def my_function():
    a = 2

my_function()
print(a)

page_break()

print('Question 7 this will print the global variable 2. global variable is reassigned when we call the function because we used the global keyword ')

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

page_break()

print('Question 8 we\'ll get an error becuase greeeting isn\'t initialized until after the print  ')
'''
print(greeting)

greeting = 'Hello world!'
'''

page_break()

print('Question 9 it\'ll print 7 becuase the function didn\'t return the equation  ')

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

page_break()

print('Question 10 it\'ll print [1, 2, 3] in order to change the list we need to use the global keyword - this is incorrect lists can be modified inside of a function\n\
if we tried to change b and not an index of b then we would need to use the global keyword')

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)