'''
 Closest pair (100 Marks)
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.

Input Format
You will be given a function with two integer arrays of size N,M respectively and a number x as arguments.

Constraints
1 < N,M < 10^3
1 < A[],B[] < 10^5

Output Format
You need to return the sum of the two numbers from the given function.

Sample TestCase 1
Input
4
1
4
5
7
4
10
20
30
40
32
Output
31
Explanation

1 and 30 is the pair whose sum is closest to x.

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n =  int(input().strip())
	alist = [int(input().strip()) for x in range(n)]
	m = int(input().strip())
	blist =[int(input().strip()) for x in range(n)]
	trg = int(input().strip())
	closest =[]

	for x in range(n):
		for y in range(m):
			if (alist[x]+blist[y])//10 == trg//10 or (alist[x]+blist[y] )>= trg:
				closest.append(alist[x]+blist[y])


	diff = abs(min(closest) - trg)
	v = 0

	for x in closest:
		if diff == 0 :
			stdout.write(str(x))
			break 

		if abs(x-trg) <= diff:
			diff = abs(x-trg)
			v = x

	stdout.write(str(v))


main()