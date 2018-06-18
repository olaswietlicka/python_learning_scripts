def blackjack(a,b,c):
	# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
	if a<1 or b<1 or c<1 or a>11 or b>11 or c>11:
		print('Numbers should be between 1 and 11')
		return False
	if a+b+c<=21:
		return a+b+c
	elif a+b+c>21 and (a==11 or b==11 or c==11):
	# elif 11 in [a,b,c] and...
		return a+b+c-10
	else:
		return 'BUST'

suma = blackjack(5,6,7)
print(suma)

suma = blackjack(9,9,9)
print(suma)
print(type(suma))

suma = blackjack(9,9,11)
print(suma)