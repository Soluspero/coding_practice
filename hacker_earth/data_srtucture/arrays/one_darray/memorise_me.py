from collections import Counter

def main():
	num = int(input())
	numlist = list(map(int,input().strip().split()))
	findQ = Counter(numlist)

	q = int(input())
	for x in range(q):
		inp = int(input())
		res = findQ[inp] if inp in findQ.keys() else None
		if res == None:
			print("NOT PRESENT")
		else:
			print(res)

if __name__ == '__main__':
	main()