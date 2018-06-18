def animal_crackers(s):
	# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
	s = s.split()
	if len(s)==1 or len(s)>2:
		print('You should write two words, not more or less')
		return False
	if s[0][0].lower() == s[1][0].lower():
		return True
	else:
		return False
	# zamiast drugiego if-a: return s[0][0].lower() == s[1][0].lower()
	# można też zrobić lower tak: s.lower().split()


a = animal_crackers('ala ala')
print(a)
a = animal_crackers('ala Ala')
print(a)
a = animal_crackers('ala ola')
print(a)
a = animal_crackers('ala Ala ola')
print(a)
a = animal_crackers('ala')
print(a)
