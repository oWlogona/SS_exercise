"""
Define a function sum() and a function multiply() 
that sums and multiplies (respectively) all the numbers in 
a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, 
and multiply([1, 2, 3, 4]) should return 24.
"""

def sume(boxe=0):
	if len(boxe):
		answer = 0
		for item in boxe:
			answer += item
		return answer
	return 0

def multiplies(boxe=0):
	if len(boxe):
		answer = 1
		for item in boxe:
			answer *= item
		return answer
	return 0


if __name__ == "__main__":
	print(sume([1, 2, 3, 4]))
	print(multiplies([1, 2, 3, 4]))