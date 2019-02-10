import timeit

"""
sample input
2
3 4
1 2 5
3 2
2 5 5
"""

def test():
	with open("test_input.txt") as f:
		n = int(f.readline().strip())

		for i in range(n):
			N, K = map(int,f.readline().strip().split())
			arr = list(map(int,f.readline().strip().split()))
			m = min(arr)
			print(K - m if K > m else 0)
			

def main():
	print(timeit.timeit(stmt="test()", setup="from __main__ import test",number=20))

if __name__ == '__main__':
	main()