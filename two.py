#two.py

import one

print("Top level in two.py")

one.func()

print('TWO:' + __name__)

if __name__ == "__main__":
	print('Two.py is directly')
else:
	print('Two.py has been imported')