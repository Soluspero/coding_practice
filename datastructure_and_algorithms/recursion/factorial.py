"""
Find factorial of a number.
"""
"""
Reverse string recursively
"""

def fact(num):
	if num == 1 or num == 0:
		return 1
	return  num * fact(num-1)

def main():
	
	print(fact(10))

if __name__ == '__main__':
	main()