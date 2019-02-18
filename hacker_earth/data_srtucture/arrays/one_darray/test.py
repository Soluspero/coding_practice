def test():
	n ={}
	l = [17,17,2,2,5,2]
	for x in l:
		if x not in n.keys():
			n[x]=1
		else:
			n[x]+=1

	print(n)
	print(sorted(n.items(),key=lambda x : x[1]))

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test",number=1))