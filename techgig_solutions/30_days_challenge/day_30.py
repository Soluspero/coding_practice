'''
 Which row is bigger? (100 Marks)
For this challenge, you need to take a matrix as an input from the stdin, identify which row has the maximum sum of the digits.For example, in the below matrix
1 2 3
4 5 6
7 8 9
Row 1 is 1,2,3
Row 2 is 4,5,6
Row 3 is 7,8,9

Input Format
The first line contains two integers N, M denoting the number of rows and columns respectively.
Each of the 'N' Next line contains M integers each.

Constraints
1 < (n,m) < 100

Output Format
If the sum of the digits of row 1 found to be greater than that of row 2 and row 3, then print 'Row 1' to the stdout. If the sum of all the rows found to be equal, then print 'Equal' to the stdout. 

Sample TestCase 1
Input
3 4
2 3 4 2
1 4 6 5
4 8 9 6

Output
Row 3

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def main():
	row,col=input().strip().split()
	alist=[[0] * int(col) for i in range(int(row))]

	for ir in range(int(row)):
		for ic,cv in enumerate(list(map(int,input().strip().split()))):
		    alist[ir][ic] = cv

	rows = dict()
	for r in range(1,int(row)+1):
		rows["Row "+str(r)] = sum(alist[r-1])

	equal = set(rows.values())

	if len(equal) != 1:
		stdout.write(max(rows))
	else:
		stdout.write("Equal")



main()

