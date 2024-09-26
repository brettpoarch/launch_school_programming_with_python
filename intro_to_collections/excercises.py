# excercise 1 If you have a list named people, how can you determine the number of entries in that list?

people = ['Brett' , 'Regina', 'Behr']
print(f'there are {len(people)} entries in the people list')

print('you can use len() to determine the number of entries in a list')

print('-' * 45)

# excercise 2 Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

print('I don\'t believe it is possible to change the value bye to goodbye in the tuple becuase tuples are immutable')

print('-' * 45)

# excercise 3 Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

print('Tuples and list are both ordered and can contain any type of data \n\
tuples and lists are different in that tuples are immutable and lists are mutable. tuple use () and list use [] ')

print('-' * 45)

# excercise 4 Why can we treat strings as sequences?

print('we can treat strings like sequences because they can be indexed ')

print('-' * 45)

# excercise 5 How do the set types differ from the sequence types?

print('sets differ from sequence types because they are unordered have unique elements and they can\'t be indexed. ')

print('-' * 45)

# excercise 6 Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.

pi = 3.141592
string_pi = str(pi)

print(type(string_pi))

print('-' * 45)

# excercise 7 Without running the following code, identify the numbers that are included in each of the following ranges:

print('0-6\n\
1-5\n\
3,7,11\n\
empty\n\
8-4')

print('-' * 45)

# excercise 8 How would you print all the numbers in the following range?

r = range(3, 17, 4)
print(list(r))

print('-' * 45)

# excercise 9 Given the below code, answer the following questions and explain your answers:
# Are the lists assigned to my_list and another_list equal?
# Are the lists assigned to my_list and another_list the same object?
# Are the nested lists at index 3 of my_list and another_list equal?
# Are the nested lists at index 3 of my_list and another_list the same object?

# my_list = [1, 2, 3, [4, 5, 6]]
# another_list = list(my_list)

print('Yes, they are equal\n\
No, they are not the same object\n\
Yes, index 3 of both lists are equal\n\
Yes, they are the same object ')

print('-' * 45)

# excercise 10 Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.
# names = { 'Chris', 'Clare', 'Karis', 'Karl',
#          'Max', 'Nick', 'Victor' }
# print(names)

print('It may not. Sets are unordered collection types')

print('-' * 45)

# excercise 11 You need to write some Python code to determine the country name associated with one of the listed names. 

names_and_countries = {
	'Alice' : 'USA', 
	'Francois' : 'Canada', 
	'Inti' : 'Peru', 
	'Monika' : 'Germany', 
	'Sanyu' : 'Uganda',
	'Yoshitaka' : 'Japan',
}

print(names_and_countries['Inti'])