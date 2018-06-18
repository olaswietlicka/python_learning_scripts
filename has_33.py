def has_33(nums):
	# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
	for i in range(1,len(nums)):
		if int(str(nums[i-1])[-1])==3 and int(str(nums[i])[0])==3:
			return True
		else:
			continue
		# to else jest przecież niepotrzebne...
	return False

a = has_33([1, 3, 3])
print(a)

a = has_33([1, 33, 3])
print(a)

a = has_33([124, 3, 4])
print(a)

a = has_33([320, 3, 304])
print(a)