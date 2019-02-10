def test():
	n = 6
	l = [16,17,4,3,5,2]
	i =0
	while i!=n-1:
		if l[i+1] > l[i]:
			print(l[i+1],end=" ")
		i+=1
	print(l[-1])

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test",number=1))