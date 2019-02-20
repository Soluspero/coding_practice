''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
INPUT
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

OUTPUT
2 4 6 8 10 12 14 16
"""
from sys import stdout
def main():

 # Write code here 
 row, col = [int(x) for x in input().strip().split()]
 alist = []

 for r in range(row):
 	for c in list(map(int,input().strip().split())):
 		if c % 2==0:
 			alist.append(str(c))

 stdout.write(" ".join(alist))

main()

