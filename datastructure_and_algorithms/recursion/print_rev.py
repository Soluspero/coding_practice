"""
Print 1 to n values in reverse.
"""
def printInc(n):
	if n > 0:
		printInc(n-1)
		print(n,end = " ")


def printRev(n):
	if n == 1 :
		return 1

	print(n, end=" ")
	return printRev(n-1)

def main():
	
	print(printRev(10))
	print(printInc(7))

if __name__ == '__main__':
	main()