
def bubbleSort(seqns):
	n = len(seqns)

	for i in range(n,0,-1):
		for j in range(i-1):
			if seqns[j] > seqns[j+1]:
				seqns[j], seqns[j+1] = seqns[j+1], seqns[j]

	return seqns


def main():
	ll = [44,22,55,11,33]

	print(bubbleSort(ll))

if __name__ == '__main__':
	main()