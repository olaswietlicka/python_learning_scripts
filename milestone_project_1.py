# milestone_project_1

print('Welcome to Tic Tac Toe!')

player_1 = 'v'
while player_1 not in ['X', 'O', 'x', 'o']:
	player_1 = input('Player 1: Do you want to be X or O?\n')
	if player_1 not in ['X', 'O', 'x', 'o']:
		print('You were supposed to choose X or O')

player_1 = player_1.upper()

if player_1 in ['X', 'x']:
	player_2 = 'O'
else:
	player_2 = 'X'

def ifwon(player,ind):
	# funkcja, która sprawdza wygraną
	thirds = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
	for i in range(0,8):
		if ind[thirds[i][0]]==player and ind[thirds[i][1]]==player and ind[thirds[i][2]]==player:
			if player==player_1:
				print('Congrats player 1, you won!')
				return True
			elif player==player_2:
				print('Congrats player 1, you won!')
				return True
	return False

def draw_table(ind = ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
	print('   |   |   ')
	print(f' {ind[0]} | {ind[1]} | {ind[2]} ')
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(f' {ind[3]} | {ind[4]} | {ind[5]} ')
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(f' {ind[6]} | {ind[7]} | {ind[8]} ')
	print('   |   |   ')

# flaga - dopóki jest False, to wpisujemy w tablicę
flaga = True
ind = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('Player 1 - you start')

indeksy = []
k = 0
while flaga:
	if k==0:
		draw_table()
	pos_1 = input('Player 1 - choose your position (1-9):\n')
	while pos_1 in indeksy:
		print('Error! This position is already taken!')
		print('Choose again')
		pos_1 = input('Player 1 - choose your position (1-9):\n')
	indeksy = [indeksy, pos_1]
	ind[int(pos_1)-1] = player_1
	draw_table(ind)
	a = ifwon(player_1,ind)
	print(a)
	if a:
		break
	pos_2 = input('Player 2 - choose your position (1-9):\n')
	while pos_2 in indeksy:
		print('Error! This position is already taken!')
		print('Choose again')
		pos_2 = input('Player 1 - choose your position (1-9):\n')
	indeksy = [indeksy, pos_2]
	ind[int(pos_2)-1] = player_2
	draw_table(ind)
	a = ifwon(player_2,ind)
	print(a)
	if a:
		break
	k+=1



