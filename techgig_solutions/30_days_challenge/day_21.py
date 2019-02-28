"""
 Multiplication between odd and even (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to find the numbers that are odd, add them. find the numbers that are even add them and then multiply the two values that you get after addition of even numbers and that of addition of odd numbers.

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line. 

Constraints
1<  N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after multiplication to the stdout. 

Sample TestCase 1
Input
6
11 22 33 44 55 66

Output
13068
Explanation

Of all the given elements which are in the array, identify numbers that are odd and add them. Identify even numbers and add them. Multiply two values that you get after addition of odd numbers and even numbers. 
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
 n = int(input().strip())
 splist = list(map(int,input().strip().split()))
 odd , even = 0 , 0
 for x in splist:
 	if (x%2==0):
 		even+=x
 	else:
 		odd+=x

 print(even*odd)

main()

