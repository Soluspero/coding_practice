import timeit

"""
sample input
6
16 17 4 3 5 2
output 
17 5 2
"""

def test():
	with open("test_input.txt") as f:
		n = int(f.readline().strip()) #int(input().strip())
		l = list(map(int,f.readline().strip().split())) ##map(int,input().strip().split())
		f = []
		pos =l[-1]
		f.append(pos)
		s = n-1
		for x in range(s,0,-1):
			if l[x-1] >= pos:
				pos = l[x-1]
				s = x-1
				f.append(l[x-1])
		print(" ".join(map(str,sorted(f,reverse=True))))
			

def main():
	print(timeit.timeit(stmt="test()", setup="from __main__ import test",number=1))

if __name__ == '__main__':
	main()