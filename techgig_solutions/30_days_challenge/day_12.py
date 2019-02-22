''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
DAY-12 : Patch up two matrices
"""
from sys import stdout
def main():

 # Write code here 
 row, col = [int(x) for x in input().strip().split()]
 alist = [[0]*col for _ in range(row)]

 for r in range(row):
 	for ci , cv in enumerate(list(map(int,input().strip().split()))):
 		alist[r][ci]= cv
 		
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

