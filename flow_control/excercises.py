# excercise 1 To what values do the following expressions evaluate?
print('1 False - \
	  2 True - \
	  3 True - incorrect. correct answer is 3 \
	  4 True - incorrect. correct answer is 3 \
	  5 False - \
	  6 True - \
	  7 False - \
	  8 False - \
	  9 True - incorrect. correct answer is false \
	  10 True')

print('-' * 45)

# excercise 2 Write a function, even_or_odd, that determines whether its argument is an even or odd number.
# If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

def even_or_odd(num):
	if num % 2 == 0:
		print('even')
	else:
		print('odd')

even_or_odd(2)
even_or_odd(3)

print('-' * 45)

# excercise 3 Without running the following code, what does it print? Why?

'''
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)
'''


print('1 - the first call to bar_code_ scanner is passing the argument "113" that parameter will match case 2 "113" and print("product2")\n\
2 - the second call passes the argument 142 as an integer. the function parameter is turned into a str and should match case 142 and print("product3") - \n\
my initial thought on question 2 was incorrect the argument did pass through as a int and therefore the parameter did not match any case and the default\
Product not found! was printed')


print('-' * 45)

# excercise 4 Refactor this statement to use a regular if statement instead.

#return ('bar' if foo() else qux())

print('if foo():\n\
	return "bar"\n\
else:\n\
	return qux()')

print('-' * 45)

# excercise 5 What does this code output, and why?


def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])


print('is_list_empty is passing the argument [] which is an empty list. empty lists evaluate to falsy which should bypass the if statement, trigger the else and print Empty')

print('-' * 45)

# excercise 6 Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. 
# Otherwise, it should return the original string.

def all_caps_over_ten(phrase):
      if len(phrase) > 10:
            return phrase.upper()
      else:
            return phrase
      
print(all_caps_over_ten('hello world'))
print(all_caps_over_ten('goodbye'))

print('-' * 45)

# excercise 7 Write a function that takes a single integer argument and prints a message that describes whether:?

def number_range(integar):
      
	  match integar:
              case integar if integar < 0:
                    print(f'{integar} is less than 0')
              case integar if integar < 51:
                    print (f'{integar} is between 0 and 50')
              case integar if integar < 101:
                    print(f'{integar} is between 51 and 100')
              case _:
                    print(f'{integar} is greater than 100')
                    
number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0