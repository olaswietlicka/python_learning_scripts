def almost_there(n):
	# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
	if (n>=90 and n<=110) or (n>=190 and n<=210):
		return True
	else:
		return False
	# return abs(100-n)<=10 or abs(200-n)<=10

a = almost_there(90)
print(a)

a = almost_there(104)
print(a)

a = almost_there(150)
print(a)

a = almost_there(100)
print(a)

a = almost_there(15)
print(a)

a = almost_there(195)
print(a)

a = almost_there(200)
print(a)

a = almost_there(205)
print(a)

a = almost_there(300)
print(a)