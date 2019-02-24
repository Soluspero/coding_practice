"""
Find product of two numbers recursively
"""

def product(x,y):
	if y == 0 :
		return 0
	return x + product(x,y-1)

def main():
	
	print(product(5,4))

if __name__ == '__main__':
	main()