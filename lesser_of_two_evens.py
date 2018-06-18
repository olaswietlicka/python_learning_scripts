def lesser_of_two_evens(a,b):
	#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
	if a==b:
		print('your numbers are equal')
		return (a,b)
	elif a%2==0 and b%2==0 and a!=b:
		if a<b:
			return a
		else:
			return b
		# wystarczy: return min(a,b)
	elif a%2==1 or b%2==1:
		if a>b:
			return a
		else:
			return b
		# wystarczy: return max(a,b)


a = lesser_of_two_evens(1,1)
print(a)
a = lesser_of_two_evens(1,2)
print(a)
a = lesser_of_two_evens(2,4)
print(a)
a = lesser_of_two_evens(2,5)
print(a)