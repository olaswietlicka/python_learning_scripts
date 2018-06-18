def spy_game(ints):
	for i in range(0,len(ints)-2):
		if '0' in str(ints[i]):
			for j in range(i+1,len(ints)-1):
				if '0' in str(ints[j]):
					for k in range(j+1,len(ints)):
						if '7' in str(ints[k]):
							return True
	return False
	# masakra...
	# code = [0,0,7,'x']
	# for num in ints:
	#		if num == code[0]:
	#			code.pop(0)
	# return len(code) == 1


s = spy_game([1,2,4,0,0,7,5])
print(s)

s = spy_game([1,0,2,4,0,5,7])
print(s)

s = spy_game([1,7,2,0,4,5,0])
print(s)

s = spy_game([10, 0, 7,2,0,4,5,0])
print(s)