"""
Print fibonacci series.
"""

def fibo(n):
	if n <=1 :
		return n
	else:
		return fibo(n-1) + fibo(n-2)

def main():
	
	for x in range(10):
		print(fibo(x),end = " ")
	print()

if __name__ == '__main__':
	main()