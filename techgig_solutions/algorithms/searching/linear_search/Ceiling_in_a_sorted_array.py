'''
 Ceiling in a sorted array (100 Marks)
Find ceil of given element in sorted array.

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. On another line, there will be another integer whose floor needs to be calculated. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5
1 < K < 10^5

Output Format
You need to print the floor of the given element if not found print -1 to the STDOUT. 

Sample TestCase 1
Input
7
1 2 8 10 10 12 19
5
Output
8
Explanation

The ceiling of x is the smallest element in array greater than or equal to x.

'''
'''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = list(map(int,input().strip().split()))
	trg = int(input().strip())
	flag =False

	for x in splist:
		if x > trg or x == trg:
			flag = True
			trg = x
			break

	if flag is True:
		stdout.write(str(trg))
	else:
		stdout.write(str("-1"))


main()


