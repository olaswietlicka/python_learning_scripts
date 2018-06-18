def old_macdonald(s):
	# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
	if len(s.split())>1:
		print('You were supposed to give a single word string')
		return False
	new_s = ''
	if len(s)<4:
		print('The word is too short, so I will change only the first letter')
		new_s = s[0].upper() + s[1:len(s)]
		return new_s
	else:
		new_s =  s[0].upper() + s[1:3] + s[3].upper() + s[4:len(s)]
		return new_s
	# można też użyć metody .capitalize(), której wcześniej nie było :) ta funkcja zmienia pierwszą literę na wielką

new_s = old_macdonald('ola')
print(new_s)

new_s = old_macdonald('ola swietlicka')
print(new_s)

new_s = old_macdonald('oleczka')
print(new_s)