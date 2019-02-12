"""
sample input 1
3
3 2 1
1 3 2
output 1:
5

Sample input 2
10
5 4 8 9 1 6 3 2 7 10
1 6 8 9 5 4 10 3 2 7

output 2:
27
"""
import timeit

def mygen(calling_order, ideal_order):
	time_taken = 0
	n = len(ideal_order)
	while calling_order != ideal_order:
		for x in calling_order:
			if calling_order.index(x) != ideal_order.index(x):
				t = x
				for y in range(calling_order.index(x),n-1):
					calling_order[y] = calling_order[y+1]
				calling_order[-1] = t
				time_taken+=1
				yield time_taken
				break


def test():
	with open("test_input.txt") as f:
		n = int(f.readline().strip()) #int(input().strip())
		calling_order = list(map(int,f.readline().strip().split())) ##list(map(int,input().strip().split()))
		ideal_order = list(map(int,f.readline().strip().split())) ##list(map(int,input().strip().split()))
		time_taken = n

		if calling_order == ideal_order:
			print(time_taken)
		else:
			time_taken+= max(list(mygen(calling_order,ideal_order)))
			# while calling_order != ideal_order:
			# 	# print("before ",ideal_order,calling_order)
			# 	for x in calling_order:
			# 		if calling_order.index(x) != ideal_order.index(x):
			# 			t = x
			# 			for y in range(calling_order.index(x),n-1):
			# 				calling_order[y] = calling_order[y+1]
			# 			calling_order[-1] = t
			# 			time_taken+=1
			# 			# print("after ",x,ideal_order,calling_order)
			# 			break

		print(time_taken)
			

def main():
	print(timeit.timeit(stmt="test()", setup="from __main__ import test",number=1))

if __name__ == '__main__':
	main()