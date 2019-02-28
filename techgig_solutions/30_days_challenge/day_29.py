'''
 Comparison between diagonals (100 Marks)
For this challenge, you need to take a matrix as an input from the stdin , calculate the sum of the digits for each diagonal and compare them.For example,
in the below matrix
1 2 3
4 5 6
7 8 9
Diagonal 1 is 1,5,9.
Diagonal 2 is 3,5,7.

Input Format
A matrix is to be taken as input from stdin.On first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space. 

Constraints
1 < (n,m) < 100

Output Format
If sum of digits for diagonal 1 is found to be greater than diagonal 2, then print 'Diagonal 1' to the stdout. If sum of digits for diagonal 2 is found to be greater than diagonal 1, then print 'Diagonal 2' to the stdout. If both of the diagonal found to be equal, then print 'Equal' to the stdout. 

Sample TestCase 1
Input
3 3
2 3 4
1 4 6
3 8 9

Output
Equal

Explanation

The sum of the digits for the diagonal 1 is 15 and that of diagonal 2 is also same i.e 15. Thus, print 'Equal' to the stdout.

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def get_diag1(n,arrlist):
	diag1 = []
	for i in range(n):
		for j in range(n):
			if i==j :
				diag1.append(arrlist[i][j])
	return diag1


def get_diag2(n,arrlist):
	diag2=[]
	for i in range(n):
			n = n -1
			diag2.append(arrlist[i][n])
	return diag2

def main():
	row,col=input().strip().split()
	alist=[[0] * int(col) for i in range(int(row))]

	for ir in range(int(row)):
		for ic,cv in enumerate(list(map(int,input().strip().split()))):
		    alist[ir][ic] = cv

	diag1 = sum(get_diag1(int(row),alist))
	diag2 = sum(get_diag2(int(row),alist))

	if diag1 > diag2:
		stdout.write("Diagonal 1")
	elif diag2 > diag1:
		stdout.write('Diagonal 2')
	else:
		stdout.write("Equal")

main()

