"""
Write a function game() number-guessing game, that takes 2 
int parameters defining the range. Using random.randint(A, B) 
generate random int from the range. While user input isn't equal that 
number, print "Try again!". If user guess the number, 
congratulate him and exit. (use raw_input())
"""


import random

def game(a=0, b=5):
	password = random.randint(a, b)
	while True:
		try:
			answer = int(input('Enter your number: '))
			if answer == password: break
		except ValueError:
			print('Only integer')
	
if __name__ == "__main__":
	game()