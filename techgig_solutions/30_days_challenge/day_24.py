"""
 Play With Average (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to find the average of even numbers, then the average of odd numbers and add them (round the averages to the nearest integers).

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after addition of the two averages to the stdout. 

Sample TestCase 1
Input
6
11 22 33 44 55 66
Output
77
Explanation

You will print the value after addition of the two averages to the stdout. 
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 splist = list(map(int,input().strip().split()))
 odd , even = 0 , 0
 ecount, ocount=0,0
 for x in splist:
    if (x%2==0):
        even+=x
        ecount+=1
    else:
        odd+=x
        ocount+=1
 stdout.write(str(round(even/ecount + odd/ocount)))

main()