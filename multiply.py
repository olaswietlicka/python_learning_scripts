def multiply(numbers):
	# Write a Python function to multiply all the numbers in a list.
	result = 1
	for num in numbers:
		result *= num
	return result

result = multiply([1,2,3,-4])
print(result)
