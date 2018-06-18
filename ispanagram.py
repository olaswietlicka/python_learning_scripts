import string

def ispanagram(s, alphabet = string.ascii_lowercase):
	alphabet = list(alphabet)
	for letter in s:
		if letter.lower() in alphabet:
			alphabet.pop(alphabet.index(letter.lower()))
	return len(alphabet)==0

check = ispanagram("The quick brown fox jumps over the lazy dog")
print(check)

check = ispanagram("kupa")
print(check)
