#Note: In binary search, sequences must be in sorted order before searching

def binarySearch(seqns, target):
	low = 0
	high = len(seqns)-1

	while low <= high:
		mid = (low+high)//2

		if seqns[mid] == target:
			return True
		elif target < seqns[mid]:
			high = mid  -1 
		else:
			low = mid + 1
	return False


def main():
	ll = [11,22,33,44,55,66] 

	if binarySearch(ll, 33):
		print("Value found")
	else:
		print("Not found!!!")


if __name__ == '__main__':
	main()