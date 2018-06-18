def summer_69(nums):
	# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
	if nums == []:
		return 0
	else:
		while (6 in nums) and (9 in nums):
			# print(list(range(nums.index(9),nums.index(6)-1,-1)))
			for i in range(nums.index(9),nums.index(6)-1,-1):
				nums.pop(i)
	return sum(nums)

suma = summer_69([1, 3, 5])
print(suma)

suma = summer_69([4, 5, 6, 7, 8, 9])
print(suma)

suma = summer_69([2, 1, 6, 9, 11])
print(suma)

suma = summer_69([2, 1, 6, 9, 11, 6, 9, 12])
print(suma)