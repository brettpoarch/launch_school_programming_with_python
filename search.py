numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0
found = -1

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break

    index += 1

print(found_item)

for number in numbers:
    found += 1
    if number == 5:
          break
    
print(found)

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

upper_cat_names = [cat.upper()
                 for cat in cats_colors]

print(upper_cat_names)