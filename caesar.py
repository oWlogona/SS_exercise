"""
Define a function caesar_cipher that takes string and key(number), whuch returns encrypted string
"""
def caesar_cipher(line='', value=0):
	if len(line):
		new_line = ''
		for item in line:
			new_line += chr(ord(item)+value)
		return new_line
	return False

def check_cipher(line='', value=0):
	if len(line):
		new_line = ''
		for item in line:
			new_line += chr(ord(item)-value)
		return new_line
	return False



if __name__ == "__main__":
	print(caesar_cipher('Martinus', 5))
	print(check_cipher(caesar_cipher('Martinus', 5), 5))