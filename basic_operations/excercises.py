# excercise 1 concatenate 2 strings with first and last name to create full name
first_name = 'Brett'
last_name = 'Poarch'
full_name = first_name + ' ' +  last_name
print('excercise 1, my first name is', first_name, 'my last name is', last_name,  'my full name is',  full_name)

print('-' * 45)

# excercise 2 extract individual digits of 4936:
print(4936 % 10)
print(4936 // 10 % 10)
print(4936 // 10 // 10 % 10)
print(4936 // 10 // 10 // 10)

print('-' * 45)

# excercise 3 code explanation
print('excercise 3, because we are concatenating two strings the result of print("5" + "10") is 510')
print('5' + '10')

print('-' * 45)

# excercise 4 refactor code from excercise 3 and use coercion to print 15
print('excercise 4, we can use coercion to convert the str to int and get the answer 15 by using print(int("5") + int("10"))')
print(int('5') + int('10'))

print('-' * 45)

# excercise 5 Will an error occur if you try to access a list element with an index greater than or equal to the list's length?
foo = ['a', 'b', 'c']
# print(foo[3])
print('excercise 5, yes we will get an error that our list index is out of range')

print('-' * 45)

# excercise 6 what value will the following expression evalute?
print('excercise 6, the expression "foo" == "Foo" will evaluate to False')
print('foo' == 'Foo')

print('-' * 45)

# excercise 7 what will the following code do and why
print('excercise 7, the code int("3.1415") will cause an error because 3.1415 would need to be coerced to a float')
print(type('3.1415').__name__)
#print(type(int('3.1415')))

print('-' * 45)

# excercise 8 what value does the following expression evaluate
print('excercise 8, the expression "12" < "9" will evaluate to True because they are being evaluated as a str one char at a time and "1" < "9"')
print("12" < "9")