import timeit
from collections import Counter

"""
sample input
5
1 1 1 2 2
output 
17 5 2
"""

def test():
	with open("test_input.txt") as f:
		n = int(f.readline().strip()) #int(input().strip())
		# l =  ##list(map(int,input().strip().split()))
		l = Counter(list(map(int,f.readline().strip().split())))
		m = max(l.values())
		print(list(l.keys())[list(l.values()).index(l.most_common(1)[0][1])])
			

def main():
	print(timeit.timeit(stmt="test()", setup="from __main__ import test",number=1))

if __name__ == '__main__':
	main()