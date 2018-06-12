print('Hello, this is a simple game,\nwhere you have to guess numbers')
print('The number should be between 1 and 100')
print("If you are close enough (less than 10) I will say 'WARM'")
print("Otherwise I will say 'COLD'")
print("And then 'WARMER' or 'COLDER' if you get closer or further")

from random import randint

my_number = randint(1,100)

guessed_number = int(input('Guess your number: '))

#print(my_number)

if guessed_number==my_number:
	print('You did it at the very first try!')

k = 0

	#print('Congrats! You have guessed the number')
	#print('You did it in {} moves'.format(k))
if guessed_number<1 or guessed_number>100:
	print('You should pick a number between 1 and 100')
	guessed_number = int(input('Guess again: '))
	k += 1
elif abs(guessed_number-my_number)>10:
	print('COLD!')
	prev_guessed_number = guessed_number
	guessed_number = int(input('Guess again: '))
	k += 1
	if guessed_number==my_number:
		print('Congrats! You have guessed the number')
		print('You did it in {} moves'.format(k))
	elif guessed_number<1 or guessed_number>100:
		print('You should pick a number between 1 and 100')
		guessed_number = int(input('Guess again: '))
		k += 1
elif abs(guessed_number-my_number)<=10:
	print('WARM!')
	prev_guessed_number = guessed_number
	guessed_number = int(input('Guess again: '))
	k += 1
	if guessed_number==my_number:
		print('Congrats! You have guessed the number')
		print('You did it in {} moves'.format(k))
	elif guessed_number<1 or guessed_number>100:
		print('You should pick a number between 1 and 100')
		guessed_number = int(input('Guess again: '))
		k += 1

while guessed_number!=my_number:
	if abs(guessed_number-my_number)>abs(prev_guessed_number-my_number):
		print('COLDER!')
		prev_guessed_number = guessed_number
		guessed_number = int(input('Guess again: '))
		k += 1
		if guessed_number==my_number:
			print('Congrats! You have guessed the number')
			print('You did it in {} moves'.format(k))
		elif guessed_number<1 or guessed_number>100:
			print('You should pick a number between 1 and 100')
			guessed_number = int(input('Guess again: '))
			k += 1
	else:
		print('WARMER!')
		prev_guessed_number = guessed_number
		guessed_number = int(input('Guess again: '))
		k += 1
		if guessed_number==my_number:
			print('Congrats! You have guessed the number')
			print('You did it in {} moves'.format(k))
		elif guessed_number<1 or guessed_number>100:
			print('You should pick a number between 1 and 100')
			guessed_number = int(input('Guess again: '))
			k += 1

