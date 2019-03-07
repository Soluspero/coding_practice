'''
 Huge Array Sorting (100 Marks)
Given an array of numbers of size n. It is also given that the array elements are in range from 0 to N^2. Sort the given array in linear time.

Input Format
You will be given an array of integers of size N.

Constraints
1 < N < 10^3
1 < A[i] < 10^6

Output Format
You need to print sorted integer array elements separated by space.

Sample TestCase 1
Input
5
0
23
14
12
9
Output
0
9
12
14
23
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

val = 0

def linearTime(x, b, i=0, s=0):
	global val
	val =s
	if x > 0:
		r = x%10
		linearTime(x//10, b, i+1, s+r*b**i)
  
def main():
    n =  5 #int(input().strip())
    splist = [0,23,14,12,9] # [int(input().strip()) for _ in range(n)]

    linear_list=list()

    for i in splist:
    	linearTime(i,n**2)
    	linear_list.append((i,val))

    for i in range(n-1,0,-1):
    	pos = 0
    	for j in range(1,i+1):
    		if linear_list[j] > linear_list[pos]:
    			pos = j

    	linear_list[i], linear_list[pos] = linear_list[pos], linear_list[i]

    for i in range(n):
    	print(linear_list[i][0])

main()
   

'''
from sys import stdin
def main():

 # Write code here 
    n = int(stdin.readline())
    num = [int(x) for x in stdin.read().split()]
    num.sort()
    for i in num:
        print(i)

main()
'''