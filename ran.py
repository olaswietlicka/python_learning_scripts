def ran_check(num,low,high):
	# Write a function that checks whether a number is in a given range (inclusive of high and low)
	if num>=low and num<=high:
		print(f'{num} is in the range between {low} and {high}')
	else:
		print(f'{num} is NOT in the range between {low} and {high}')

def ran_bool(num,low,high):
	# Write a function that checks whether a number is in a given range (inclusive of high and low); return a boolean
	return num>=low and num<=high

# można było użyć funkcji range

ran_check(5,2,7)
print(ran_bool(5,2,7))

ran_check(1,2,7)
print(ran_bool(1,2,7))

ran_check(2,2,7)
print(ran_bool(2,2,7))

ran_check(7,2,7)
print(ran_bool(5,2,7))

ran_check(8,2,7)
print(ran_bool(8,2,7))