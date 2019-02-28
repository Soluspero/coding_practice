"""
 Maximum Vs Minimum (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to find the minimum number and maximum number from the array and multiply them.

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after multiplication to the stdout. 

Sample TestCase 1
Input
6
11 22 33 44 55 66

Output
726
Explanation

Of all the given elements which are in the array, find the minimum number and the maximum number and multiply them. 
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 splist = list(map(int,input().strip().split()))

 stdout.write(str(min(splist)*max(splist)))

main()