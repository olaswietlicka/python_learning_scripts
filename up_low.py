def up_low(s):
	# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
	print('Original string: ' + s)
	k = 0
	j = 0
	# dla k i j można było utworzyć dictionary
	for letter in s:
		if letter.isupper():
			k += 1
		elif letter.islower():
			j += 1
	print(f'No. of Upper case characters: {k}')
	print(f'No. of Lower case characters: {j}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)