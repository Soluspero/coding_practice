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
8
"""
from sys import stdout
def main():

 # Write code here 
 row, col =  input().strip().split()
 count = 0

 for r in range(int(row)):
 	for c in list(map(int,input().strip().split())):
 		if c ==0:
 			count+=1

 stdout.write(str(count))

main()

