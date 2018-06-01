"""Define a function, which takes a string with N opening brackets 
("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it 
consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
Examples:
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK"""


def check_brackets(line=''):
	if len(line):
		brackets = {('{', '['): 0}

		for item in line:
			if item in ('{', '['):
				brackets[('{', '[')] += 1
			elif item in ('}', ']'):
				brackets[('{', '[')] -= 1

			if brackets[('{', '[')] < 0: return 'NOT OK'

		if brackets[('{', '[')] > 0: return 'NOT OK'
		else: return "OK" 
	return ''
	
if __name__ == "__main__":
	print(check_brackets('[]'))
	print(check_brackets('[{}}]'))