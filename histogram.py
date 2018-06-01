"""
Define a function histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
****
*********
******
(usage time.sleep(s) possible for better visualization)
"""

import time

def histogram(boxe=[]):
	if len(boxe):
		for item in boxe:
			time.sleep(0.7)
			print('*' * item)

	return False

if __name__ == "__main__":
	histogram([4, 9, 7])