def page_break():
	print('-' * 45)

for num in range(0, 11, 2):
	print(num)

print('Question 1 I expect the code to print 0, 2, 4, 6, 8, 10' )

page_break()

for i in range(10, -1, -1):
	if i >= 1:
		print(i)
	else:
		print('Launch!')

page_break()

greeting = 'Aloha!'

for i in range(0, 3):
	print(greeting)

page_break()

for num in range(1, 101):
	print(num * 2)

page_break()

#1st = [1, 3, 7, 15]
first = [1, 3, 7, 15]
index = 0

while index < len(first):
	print(first[index])
	index += 1
print('Question 5 1st can\'t be the name of a variable because it starts with a number so we are can\'t complete this assignment without changing the variable name')

page_break()

friends = ['Sarah', 'John', 'Hannah', 'Dave']

for friend in friends:
	print(f'Hello, {friend}!')

page_break()

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
	if city == None:
		continue
		
	print(len(city))

page_break()

while True:
	print("and on")
	break
	
page_break()

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
index = 0

for fish in fish_list:
	if fish == 'Nemo':
		print(fish)
		break

	print(fish)

while index < len(fish_list):
	print(fish_list[index])
	if fish_list[index] == 'Nemo':
		break

	index += 1

page_break()

while True:
	print('Should I stop looping?')
	answer = input().casefold()
	if answer == 'yes':
		break
