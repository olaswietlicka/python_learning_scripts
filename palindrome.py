def palindrome(word):
	# Write a Python function that checks whether a passed in string is palindrome or not.
	return word == word[::-1]

boolean = palindrome('helleh')
print(boolean)

boolean = palindrome('kupa')
print(boolean)