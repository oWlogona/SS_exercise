"""
Define a function is_palindrome() that recognizes palindromes 
(i.e. words that look the same written backwards). For example, 
is_palindrome("radar") should return True.
"""
def is_palindrome(line=''):
	if len(line):
		new_line = ''
		for i in line:
			new_line = i + new_line
		return line == new_line

	#or

	#return line == line[::-1]

if __name__ == "__main__":
	print(is_palindrome('анна'))