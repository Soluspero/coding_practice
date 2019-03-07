'''
 Pairs with constant difference (100 Marks)
Given a sorted array find total number of pairs whose difference is k.

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. On another line, there will be another integer which represents the value of k. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5
1 < K < 10^5

Output Format
You need to print the number of pairs to the STDOUT. 

Sample TestCase 1
Input
5
1 5 3 4 2
3
Output
2
Explanation

There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2}

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = list(map(int,input().strip().split()))
	trg = int(input().strip())
	count=0

	for x in range(n-1,0,-1):
		for y in range(x):
			if (abs(splist[x]-splist[y]))==trg:
				count+=1

	stdout.write(str(count))


main()