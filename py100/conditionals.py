def page_break():
	print('-' * 45)

print('Question 1 the falsy values that I can remember in Python are - None, 0, False - I misseed all the empty strings amd collections')

page_break()

import random
random_number = random.randint(0, 1)

if random_number == True:
	print('Yes')
else:
	print('no')

page_break()

print('Yes!' if random_number else 'no')

page_break()

def weather(condition):
	if condition == 'sunny':
		print('It\'s a beautiful day!' )
	elif condition == 'rainy': 
		print('Grab your umbrella' )
	else: 
		print('Let\'s stay inside')

weather('sunny')
weather('rainy')
weather('windy')

page_break()

print('Question 5 the code will print(\'neight\') because it will match \'horse\' to the \'horse\' case')

page_break()

def weather(condition):
	match condition:
		case 'sunny':
			print('It\'s a beautiful day!' )
		case 'rainy':
			print('Grab your umbrella' )
		case _:
			print('Let\'s stay inside')


weather('sunny')
weather('rainy')
weather('windy')

page_break()

print('Question 7 the code will print \'Yes!\' because False or True will return True')

if False or True:
    print('Yes!')
else:
    print('No...')

page_break()

print('Question 8 the code will print \'No\...\' because False and True will return False')

if True and False:
    print('Yes!')
else:
    print('No...')

page_break()

print('Question 9 the code will print 3.99 because Sale is True')

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

page_break()

print('Question 10 i_moving should evaluate to True because braking_force < accelation and acceleration > 0.\n\
It\s best to have the parentheses so we are telling the computer exactly how we want the conditional evaluated')

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)