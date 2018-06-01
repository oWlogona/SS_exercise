"""
Write a ship battle game, which is similar to ex.8, except it takes 1 
integer as an order of matrix, randomly generates index (x, y) and checks 
user input (2 integers).(tip: use var1, var2 = raw_input("Enter two 
numbers here: ").split()) *Visualize the game.
"""

from math import sqrt
import random


def show_area(size_area):
	for item in range(size_area):
		print('|_|'*size_area)

def game(size_area=5):
	if size_area:
		show_area(size_area)
		answer_x = random.randint(0, size_area)
		answer_y = random.randint(0, size_area)
		print('x= ', answer_x)
		print('y= ', answer_y)
		while True:
			try:
				x, y = input('Enter numbers(x,y):').split(',')
				x, y = int(x), int(y)
				if answer_x == int(x) and answer_y == int(y): return '\nCongratulations !!!\n'
				else: print('Try again !')
			except ValueError:
				print('Enter only integer !')
	return 0


	
if __name__ == "__main__":
	print(game(7))