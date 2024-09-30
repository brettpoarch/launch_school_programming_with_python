def page_break():
	print('-' * 45)


car = {
	'type' : 'sedan',
	'color' : 'blue',
	'mileage' : 80000
}

print(car)

page_break()

car['year'] = 2003

print(car)

page_break()

del car['mileage']

print(car)

page_break()

print(car['color'])

page_break()

count = 0

for key in car:
	count += 1

print(count)

print('completely blanked on using the much more concise code of just print(len(cars))')

page_break()

student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)
print('grade' in student)

page_break()



vehicles = {
	'car' : {
		'type' : 'sedan',
		'color' : 'blue',
		'year' : 2003
	},
	'truck' : {
		'type' : 'pickup',
		'color' : 'red',
		'year' : 1998
	}
}

print(vehicles)

page_break()

car = [['type', 'sedan'], ['color', 'blue'], ['year', 2003]]

print(car)

page_break()

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_number = []

for number in numbers:
	half_number.append(int(numbers[number] / 2))

print(half_number)

page_break()

for number in numbers:
	print(f'A {number} number is {numbers[number]}')

page_break()
