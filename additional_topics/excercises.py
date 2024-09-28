def page_break():
	print('-' * 45)

# excercise 1 In your own words, explain the difference between these two expressions.

print('expression 1 is checking to see if the objects have the same values. expression 2 checks to compare if they are he same object')

page_break()

# excercise 2 Without running this code, what will it print? Why?

print('I believe it will print {42, Monty Python, (a, b,c), range(5, 10)}. When we initialize set2 = set1 both variables are pointing at the same object ')

page_break()

# excercise 3 Without running this code, what will it print? Why?

print('because dict2 and dict1 are pointing at the same object when we make a change to one we will see it on the other. It should print: Holy Grail - \n\
incorrect my initial thought would be correct if dict2 = dict1 at initialization but dict2 = dict(dict2) creates a new object that has the same values as dict 1 \n\
because it is a new object changing one will not change the other')

page_break()

# excercise 4 Without running this code, what will it print? Why?

print('even though we created a new object when initializing dict2 by using dict2 = dict(dict1) I think this will print 42 because it is a shallow copy.\n\
in shallow copies nested objects still share the same pointer for both variables')

page_break()

# excercise 5 Write some code to create a deep copy of the dict1 object and assign it to dict2. You should only modify the code where indicated.
import copy 

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1) # You may modify the `???` part
            # of this line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

page_break()

# excercise 6 The following program is nearly identical to that of the previous exercise.
# However, this time, it should create a shallow copy of dict1. Be careful: you're not allowed to use the copy module in this exercise.`

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])