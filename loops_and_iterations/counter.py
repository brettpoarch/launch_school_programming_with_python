counter = 1

while counter in range(0, 10):
	print(counter)
	counter += 1 

for counter in range(0, 10):
	print(counter)

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
	if name == 'Max':
		continue

	upper_names.append(name.upper())

print(upper_names)