def page_break():
	print('-' * 45)

str = "These aren't the droids you're looking for."

print(len(str))

page_break()

str = 'confetti floating everywhere'

print(str.upper())

page_break()

name = 'Roger'

if name.casefold() == 'RoGeR'.casefold():
	print('true')
else:
	print('false')

print(name.casefold() == 'DAVE'.casefold())

page_break()

print('A pirate I was meant to be!\n\
Trim the sails and roam the sea!')

page_break()

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print('x' in char_sequence)

page_break()

def is_empty(str):
	return not str

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

page_break()

print('launch school tech & talk'.title())

page_break()

def starts_with(str, prefix):
	return str.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

page_break()

def count_substrings(str, substr):
	return str.count(substr)


print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0