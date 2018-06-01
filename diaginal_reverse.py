"""
define a function diaginal_reverse() that takes 
matrix and returns diagonal-reversed one:
1 2 3         1 4 7
4 5 6 returns 2 5 8
7 8 9         3 6 9
"""
from math import sqrt

def diaginal_reverse(boxe=[]):
	if len(boxe):
		n = sqrt(len(boxe))
		if not(n % int(n)):
			answer = []
			for i in range(int(n)):
				for tmp in boxe[i::int(n)]:
					answer.append(tmp)
			return answer
		return 'Matrice is not correct'
	return []
	
if __name__ == "__main__":
	print(diaginal_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9]))