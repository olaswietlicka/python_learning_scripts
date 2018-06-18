def master_yoda(s):
	# MASTER YODA: Given a sentence, return a sentence with the words reversed
	new_s = s.split()
	new_s = new_s[::-1]
	new_s = ' '.join(new_s)
	return new_s

new_s = master_yoda('Oleczka is not happy')
print(new_s)

new_s = master_yoda('I am home')
print(new_s)

new_s = master_yoda('We are ready')
print(new_s)