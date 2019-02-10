import time

# def mygen(arr1, arr2,n):
# 	 for i in range(int(n)):
# 	 	yield str(int(arr1[i])+int(arr2[i]))
	

def main():
	# input()
	with open("test_input.txt") as f:
		n = f.readline().strip()
		arr1 = f.readline().strip().split()
		arr2 = f.readline().strip().split()

		#solution 1
		# arr3 = []
		# for i in range(int(n)):
		# 	c = str(int(arr1[i])+int(arr2[i]))
		# 	arr3.append(c)

		#solution 2
		# arr3 = [str(int(arr1[i])+int(arr2[i])) for i in range(int(n))]
		# print(arr3)

		#solution 3
		arr3 = (str(int(arr1[i])+int(arr2[i])) for i in range(int(n)))
		print([i for i in arr3])

		#solution 4
		# print([i for i in mygen(arr1,arr2,n)])


t1 = time.clock()
main()
print(f"Time taken : {time.clock()-t1}")