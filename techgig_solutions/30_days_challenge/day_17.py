"""
 Find pairs (100 Marks)
For this challenge, you need to take array and an integer as an input, check for pair in array with sum as that of an integer and if you find those two numbers in the array return true else return false.

Input Format
You need to take an integer input on first line which tells about the size of the array.Another line will have array elements separated by spaces. Last line will have an integer input that defines the number for which the pair has to be searched in the array. 

Constraints
1 < n < 10^5
1 < A[i] < 10^5

Output Format
Print 'True' if the pair found in the array element else print 'False' to the stdout. 

Sample TestCase 1
Input

7
33 12 -76 11 9 7 6
20

Output
True
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout

def main():

 # Write code here 
 n = int(input().strip())
 alist = list(map(int,input().strip().split()))
 trg = int(input().strip())
 flag = False

 for x in range(n-1):
 	if (alist[x] + alist[x+1]) == trg:
 		flag = True
 		break

 stdout.write(str(flag))


main()