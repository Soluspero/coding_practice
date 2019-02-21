''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
INPUT
5 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20

OUTPUT
1 
5 2 
9 6 3 
13 10 7 4 
17 14 11 8 
18 15 12 
19 16 
20 
"""
from sys import stdout

def dig(start,end, col, alist):
    ll = []
    while start >=0 and end < col:
        ll.append(alist[start][end])
        start-=1
        end +=1
    return ll
		
def main():

 # Write code here 
 row, col=  input().strip().split()
 row, col = int(row),int(col)
 alist = [ [0]*col for x in range(row)]
 
 for r in range(row):
     for ci, cv in enumerate(list(map(int,input().strip().split()))):
         alist[r][ci] = cv
         
 for r in range(row):
    s=""
    for i in dig(r,0,col,alist):
        stdout.write("{:{w}}".format(str(i),w=i*2))
    if r < row:
        stdout.write("\n")

 for c in range(1,col):
    s=""
    for i in dig(row-1,c,col,alist):
        stdout.write("{:{w}}".format(str(i),w=i*2))
    if c < col:
        stdout.write("\n")

main()