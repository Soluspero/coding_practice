'''
 Linear Search (100 Marks)
Given an array of numbers of size n and integer x. Search whether x is present in array or not. If yes, return true else return false. You need to perform linear search on the given array. 

Input Format
You will be given an array of integers of size N and integer X.

Constraints
1 < N < 10^5
1 < A[i] <10^5
1 < X < 10^5

Output Format
You need to return boolean value from the given function. 

Sample TestCase 1
Input
5
0
23
14
12
9
12
Output
1

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 splist = [int(input().strip()) for _ in range(n)]
 trg = int(input().strip())
 flag = False

 for x in range(n):
 	if  splist[x] == trg:
 		flag = True
 		break

 stdout.write(str(1) if flag is True else str(0))

main()

