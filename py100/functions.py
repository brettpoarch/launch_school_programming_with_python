def page_break():
	print('-' * 45)

def multiply(num1, num2):
	return num1 * num2

print(multiply(12, 4))    # 48

page_break()

def bruce_eckel_quote():
	print('Python is executable pseudocode.')

returned = bruce_eckel_quote()

print('Question 2 the return value of the function is none')

print(returned)

page_break()

def cite(person, quote):
	print(f'{person} said: "{quote}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')

page_break()

def squared_number(num):
	return num * num

print(squared_number(3))

page_break()

print('Question 5 it wont print anything because we never actually call the function')

page_break()

def compare_by_length(str1, str2):
	if len(str1) < len(str2):
		return -1
	elif len(str1) > len(str2):
		return 1
	else: 
		return 0

print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))     #  0

page_break()

ruby = 'Captain Ruby'
python = ruby.replace('Ruby', 'Python')

print(python)

page_break()

def greet(language):

	match language:
		case 'en':
			return('Hi!')
		case 'fr':
			return('Salut!')
		case 'pt':
			return('Olá!')
		case 'de':
			return('Hallo!')
		case 'sv':
			return('Hej!')
		case 'af':
			return('Haai!')

print(greet('en'))     
print(greet('fr'))        
print(greet('pt'))        
print(greet('de'))        
print(greet('sv'))        
print(greet('af')) 

page_break()

def extract_language(locale):
	return locale[0:2]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

page_break()

def extract_region(locale):
	return locale[3:5]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

page_break()

def local_greet(language):

	match language[0:2]:
		case 'en':
			match language[3:5]:
				case 'US':
					return('Hi!')
				case 'GB':
					return('Hello!')
				case 'AU':
					return('Howdy!')
		case 'fr':
			return('Salut!')
		case 'pt':
			return('Olá!')
		case 'de':
			return('Hallo!')
		case 'sv':
			return('Hej!')
		case 'af':
			return('Haai!')

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!