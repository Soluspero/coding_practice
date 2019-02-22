"""
DAY-13: Roll your matrix
"""
from sys import stdout
def transpose(alist,row,col):
	translist=[]
	for ir in range(col):
		ll=[]
		for ic in range(row):
			ll.append(alist[ic][ir])
		translist.append(ll)
	
	return translist

def main():

 # Write code here 
 row, col = [int(x) for x in input().strip().split()]
 alist = [[0]*col for _ in range(row)]

 for r in range(row):
 	for ci , cv in enumerate(list(map(int,input().strip().split()))):
 		alist[r][ci]= cv

 alist = transpose(alist,row,col)

 for r in range(row):
 	for c in range(col):
 		print(alist[r][c],end=" ")
 	print()


main()