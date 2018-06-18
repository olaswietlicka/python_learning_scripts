def paper_doll(s):
	# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
	new_s = ''
	for i in range(0,len(s)):
		new_s = new_s + s[i]*3
		# +=!
	return new_s

a = paper_doll('Mississippi')
print(a)