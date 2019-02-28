'''
 Consecutive!!! (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to tell whether the numbers present in the array are consecutive or not.

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5

Output Format
If the array elements are consecutive, print 'True' else print 'False' to the stdout. 

Sample TestCase 1
Input
6
11 22 33 44 55 66

Output
False

Explanation
All the elements in the given array have a difference of 1 to the previous element. Thus, they are consecutive. 
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 splist = list(map(int,input().strip().split()))
 flag = False

 for x in range(n-1):
 	if (splist[x+1]-splist[x])==1:
 		flag = True
 	else:
 		flag = False
 		break

 stdout.write(str(flag))

main()