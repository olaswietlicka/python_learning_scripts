def print_big(letter):
	ast_dict = {'full':'*****','single_middle':'  *  ','single_left':'*    ','single_right':'    *','separate_ast':'* * *','separate_space':' * * ','two_sides':'*   *','four_left':'**** '}
	if letter.lower() == 'a':
		print(ast_dict['single_middle'] +'\n' + ast_dict['separate_space'] + '\n' + ast_dict['full'] + '\n' + ast_dict['two_sides'] + '\n' + ast_dict['two_sides'])
	elif letter.lower() == 'b':
		print(ast_dict['four_left'] + '\n' + ast_dict['two_sides'] + '\n' + ast_dict['four_left'] + '\n' + ast_dict['two_sides'] + '\n' + ast_dict['four_left'])


print_big('a')

print_big('b')