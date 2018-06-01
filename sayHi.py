"""
Define a function, that takes string as argument and prints "Heelo, %arg%!
"""

def main(line='word'):
	return 'Hello, {}!'.format(line)

if __name__ == "__main__":
	print(main())
