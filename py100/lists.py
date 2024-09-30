def page_break():
	print('-' * 45)

def first(list):
	if not list:
		return 'empty list'
	
	return list[0]

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))

page_break()

def last(list):
	if list:
		return list[-1]
	
	return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))

page_break()

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.remove('fossil')
energy.append('geothermal')

print(energy)

page_break()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(list(alphabet))

page_break()

scores = [96, 47, 113, 89, 100, 102]

count = 0

for score in scores:
	if score >= 100:
		count += 1

print(count)

page_break()

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for lists in vocabulary:
	for list in lists:
		print(list)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...

page_break()

print('Question 7 I believe it\'ll print True because we\'re comparing the values in list1 to list2')

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

page_break()

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print(type(some_value1))
print(type(some_value2))

page_break()

def contains(city, list):
	if city in list:
		return True
	
	return False

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

page_break()

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

new_passcode = '-'.join(passcode)

print(new_passcode)
# Write some code here.
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

page_break()

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']


#while grocery_list:
#    checked_item = grocery_list.pop(0)
#    print(checked_item)
	
for grocery in grocery_list:
	print(grocery)

grocery_list.clear()


print(grocery_list)

