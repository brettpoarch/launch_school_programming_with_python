# excercise 1 identify data type
print('excercise 1 "True" class type = ' ,  type('True'))
print('excercise 1 False class type = ' , type(False))
print('excercise 1 (1, 2, 3) class type = ' , type((1, 2, 3)))
print('excercise 1 1.5 class type = ' , type(1.5))
print('excercise 1 [1, 2, 3] class type = ' , type([1, 2, 3]))
print('excercise 1 2 class type = ' , type(2))
print('excercise 1 range(5) class type = ' , type(range(5)))
print('excercise 1 {1, 2 ,3} class type = ' , type({1, 2, 3}))
print('excercise 1 None class type = ' , type(None))
print('excercise 1 {"foo": "bar"} class type = ' , type({'foo':'bar'}))

print(('-')*45)

# excercise 2 create a tuple
names = ('Asta', 'Butterscotch', 'Pudding', 'Neptune', 'Darwin')
print('excercise 2 names class type = ' , type(names))
print('excercise 2 here is the entire names tuple ' , names)

print(('-')*45)

# excercise 3 create dictionary named pets
pets = {
	'Asta' : 'dog',
	'Butterscotch' : 'cat',
	'Pudding' : 'cat',
	'Neptune' : 'fish',
	'Darwin' : 'lizard',
}

print('excercise 3 pets class type = ' , type(pets))
print('excercise 3 here is the entire pets dictionary ' , pets)