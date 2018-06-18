def makes_twenty(a,b):
	# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
	if type(a)!=int or type(b)!=int:
		print('You were supposed to give two ints')
		return False
	if a+b==20 or a==20 or b==20:
		return True
	else:
		return False

a = makes_twenty(20,15)
print(a)

a = makes_twenty(12,8)
print(a)

a = makes_twenty(2,6)
print(a)

a = makes_twenty(25,15)
print(a)