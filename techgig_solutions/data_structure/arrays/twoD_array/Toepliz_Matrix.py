"""
 Toepliz Matrix (100 Marks)
You will be given a two-dimensional array and a number and you are asked to find whether the given matrix is Toepliz or not.

Input Format
You will be given a function with matrix as single argument. 

Constraints
1 <= n,m <= 1000

Output Format
You need to return 1 if the matrix is Toepliz, else return -1. 

Sample TestCase 1
Input
4
5
6 7 8 9 2
4 6 7 8 9
1 4 6 7 8
0 1 4 6 7

output
1

Explanation

A matrix is "Toepliz" if each descending diagonal from left to right is constant.
"""
from sys import stdout

def dig(start,end,row, col, alist):
	chk = alist[start][end]
	flag = False
	while end < col and start < row:
		if alist[start][end] == chk:
			start+=1
			end +=1
			flag = True
		else :
			flag = False
			break

	return flag

def main():

 # Write code here 
 row =  int(input().strip())
 col = int(input().strip())
 alist = [ [0]*col for x in range(row)]

 for r in range(row):
 	for ci, cv in enumerate(list(map(int,input().strip().split()))):
 		alist[r][ci] = cv

 flag = False
 for r in range(row):
 	if dig(r,0,row,col,alist) is True:
 		flag = True
 	else:
 		flag = False
 		break

 for c in range(col):
 	if dig(0,c,row,col,alist) is True:
 		flag = True
 	else:
 		flag = False
 		break
 
 stdout.write(str(1) if flag is True else str(-1))

main()

