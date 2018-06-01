"""Write a function char_freq() that takes a string and builds a 
frequency listing of the characters contained in it. Represent the frequency 
listing as a Python dictionary. Try it with something like 
char_freq("abbabcbdbabdbdbabababcbcbab")."""

def char_freq(line=''):
	if len(line):
		ans_dict = {item: 0 for item in line}
		for item in line:
			ans_dict[item] += 1
		return ans_dict
	return 'empty'
	
if __name__ == "__main__":
	print(char_freq("aaaa00fdfdlrk"))