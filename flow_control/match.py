value = 5

match value:
	case 5:
		print('value is 5')
	case 6:
		print('value is 6')
	case _: # default case
		print('value is neither 5 nor 6')

value = -1
match value:
	case 1 | 2 | 3 | 4:
		print('value is < 5')
	case 5| 6:
		print('value is 5 or 6')
	case value if value < 0:
		print('value is a negative number')

