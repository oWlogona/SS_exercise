"""
Define a function reverse() that computes 
the reversal of a string. For example, 
reverse("I am testing") should return the string "gnitset ma I".
"""

def reversed(line=''):
	if len(line):
		answer = ''
		for item in line:
			answer = item + answer
		return answer
	
	#or 
	
	#return line[::-1]

if __name__ == "__main__":
	print(reversed('Hi test'))