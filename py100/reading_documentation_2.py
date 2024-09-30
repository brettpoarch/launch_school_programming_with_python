def page_break():
	print('-' * 45)

name = "Victor"
profession = "programmer"

print('Hello, {}. You are a {}'.format(name, profession))
print(f'Hello, {name}. You are a {profession}')

page_break()

ice_cream_density = 10

while ice_cream_density > 0:
	print('Drip...')
	ice_cream_density -= 1

print('The ice cream melted.')

page_break()

print('4 * 5 + 3**2 / 10. the exponent has the highest priorty so 4 * + 9 / 10 followed by multiplication and division sharing the next highest and goint left to right \n\
so 20 + 0.9 then addition so 20.09' )
	  
print(4 * 5 + 3**2 / 10)

page_break()

from datetime import datetime

print(datetime.now())

page_break()

print('the year attribute returns just the year. isocalendar returns a tuple with year, week and weekday')

page_break()

print('str.join expects an iterable element and a TypeError will be raised if there are any non-string values in the collection.  ')

page_break()

print('we would use "in" to find if a substring exists')

page_break()

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
	
print('A syntax error indicates the program isn\'t able to read what we\'re asking it to do. in this case we need to add a : after the conditional')

page_break()

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5

print(length_of_tweet)