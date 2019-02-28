'''
 Biggest Digit In A Number (100 Marks)
For this challenge, you will take an integer input from stdin, store it in a variable, find the digits in a number and then print the biggest of them.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Constraints
1 < N < 10^9

Output Format
Print the biggest digit in a number. 

Sample TestCase 1
Input
345678

Output
8
Explanation

For the above number, firstly get the digits which is their in that number and then compare between them to get the largest digit. 

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 high =  n%10
 n = n//10

 while n !=0:
 	t = n%10
 	n = n//10

 	if t > high:
 		high = t

 stdout.write(str(high))

main()