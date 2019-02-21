"""
 Add up two matrices (100 Marks)
For this challenge, you need to take 2 matrices as an input the stdin , add them and print the resultant matrix to the stdout.

Input Format
Two matrices to be taken as an input.For each matrix, on first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space.Then after that, each line will represent will represent each row and you need to enter numbers which each rows should have separated by a space.

Constraints
1 <= n,m <= 1000

Output Format
Print the resultant matrix to the stdout each each line should represent each row and values in the row should be separated by a space.

Sample TestCase 1
Input
3 3
3 6 9
1 2 3
4 7 8

3 3
1 2 3
4 5 6
7 8 9

output:
4 8 12
5 7 9
11 15 17

Explanation

Two matrices must have an equal number of rows and columns to be added. The sum of two matrices A and B will be a matrix which has the same number of rows and columns as do A and B. The sum of A and B, denoted A + B, is computed by adding corresponding elements of A and B.
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout
def main():

 # Write code here 
 row, col = [int(x) for x in input().strip().split()]
 alist = [[0]*col for _ in range(row)]

 for r in range(row):
 	for ci , cv in enumerate(list(map(int,input().strip().split()))):
 		alist[r][ci]= cv
 
 input().strip()
 row1, col1 = [int(x) for x in input().strip().split()]
 blist = [[0]*col1 for _ in range(row1)]

 for r in range(row1):
 	for ci , cv in enumerate(list(map(int,input().strip().split()))):
 		blist[r][ci]= alist[r][ci] + cv
 
 for r in range(row):
    s = ""
    for c in range(col):
        s+= str(blist[r][c])+" "
    stdout.write(s.strip())
    
    if r < row-1:
        stdout.write("\n")

main()

