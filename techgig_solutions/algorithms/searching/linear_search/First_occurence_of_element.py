'''
 First occurence of element (100 Marks)
Given a sorted array with duplicates, find first occurrence of a given element. 

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. On another line, there will be another integer whose first occurrence needs to be identified. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5
1 < K < 10^5

Output Format
You need to print the first occurrence of the element if not found print -1 to the STDOUT. 

Sample TestCase 1
Input
9
1 2 2 2 2 2 5 7 7
2
Output
1
Explanation

The first occurrence of the element 2 is at index 1.

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = list(map(int,input().strip().split()))
	trg = int(input().strip())
	flag = False
	i = 0

	for x in range(n):
		if splist[x] == trg:
			flag = True
			i = x
			break

	stdout.write(str(i) if flag is True else str("-1"))


main()

