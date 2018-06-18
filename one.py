#one.py

def func():
	print('FUNC() in one.py')

print("Top level in one.py")

print('ONE:' + __name__)

if __name__ == "__main__":
	print('One.py is directly')
else:
	print('One.py has been imported')