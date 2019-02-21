''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
INPUT
5 5
1 2 3 4 20
5 6 7 8 30
9 10 11 12 40
13 14 15 16 50
21 22 23 24 25

OUTPUT
21 13 9 5 1 
22 14 10 6 2 
23 15 11 7 3 
24 16 12 8 4 
25 50 40 30 20
"""
from sys import stdout
def main():

 # Write code here 
 row, col = input().strip().split()
 row, col=int(row),int(col)
 alist = [[0]*col for _ in range(row)]
 
 for r in range(row):
    for ci , cv in enumerate(list(map(int,input().strip().split()))):
        alist[r][ci]= cv
 
 for r in range(row):
    s = ""
    for c in range(col-1,-1,-1):
        s += str(alist[c][r])  + " "
        
    if r < row-1:
        stdout.write(s)
        stdout.write("\n")
    else:
        stdout.write(s.strip())
    
main()