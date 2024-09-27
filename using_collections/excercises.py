def page_break():
	print('-' * 45)

# excercise 1 Write Python code to print the seventh number of range(0, 25, 3)

my_list = list(range(0, 25, 3))

print(f' The seventh number in the range is {my_list[6]}.' )

page_break()

# excercise 2 Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

my_str = 'Launch School'

print(my_str[4:10])

page_break()

# excercise 3 Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original.
# It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2)

orig_tuple = (1, 2, 3, 4, 5)

#new_tuple = orig_tuple[-2 : 0 : -1]
new_tuple = reversed(orig_tuple[1 : -1])
new_tuple = tuple(new_tuple)

print(new_tuple)

page_break()

# excercise 4 This is a 3-part question. Consider the following dictionary:
# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

page_break()

# excercise 5 Which of the following values can't be used as a key in a dict object, and why?

print('mutable objects can\'t be used as dict keys')

page_break()

# excercise 6 What will the following code print?

print(
'1 False \n\
2 False \n\
3 False \n\
4 False \n\
5 False \n\
6 True \n\
7 True \n\
8 False \n\
9 False \n\
10 False \n\
11 True - I was incorrect on this one \'\' leaves no space \' \' would be True'
)
'''
print('abc-def'.isalpha())
print('abc_def'.isalpha())
print('abc def'.isalpha())
print('abc def'.isalpha() and
      'abc def'.isspace())
print('abc def'.isalpha() or
      'abc def'.isspace())
print('abcdef'.isalpha())
print('31415'.isdigit())
print('-31415'.isdigit())
print('31_415'.isdigit())
print('3.1415'.isdigit())
print(''.isspace())
'''

page_break()

# excercise 7 Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

#info = info.split(':')     original code
#info = '+'.join(info)

#info = '+'.join(info.split(':'))  refractored to one line and mutating


print('+'.join(info.split(':')))  # print without mutating

page_break()

# excercise 8 Explain why the code below prints different values on lines 3 and 4.

print('on line 3 we\'re slicing the string which causes a new string and index. on line 4 we\'re starting at the index of 21 on the original string ' )

page_break()

# excercise 9 Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)
print(stuff[1][3])

page_break()

# excercise 10 Write one line of code to print the activities that Cocoa enjoys.

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(f'Pete\'s cat Coca enjoys {cats['Pete']['Cocoa']['enjoys']}')

page_break()

# excercise 11 Without running the following code, determine what each line should print.

print(
'1 False \n\
2 True \n\
3 True \n\
4 False \n\
5 True \n\
6 Fales \n\
7 Flase \n\
8 True \n\
9 True - incorrect sets only check whether a specific value is in the set \n\
10 True'
)

page_break()

# excercise 12 Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

page_break()

# excercise 13 Without running the following code, determine what each print statement should print.

print(
'1 True \n\
2 False \n\
3 True \n\
4 False'
)

page_break()

# excercise 14 Assume you have the following sequences:

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

zipped_iterables = list(zip(my_str, my_list, my_tuple, my_range))

print(zipped_iterables)

page_break()

# excercise 15 Without running the following code, what values will be printed by line 10?

print('I believe it\'ll print Cat Bird and Snake')

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

