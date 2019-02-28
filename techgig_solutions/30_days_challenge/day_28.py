'''
 Compare two numbers (100 Marks)
For this challenge, you will take two integers input from stdin, sum the digits of a number and same is to be done with another number. Then compare the sum of the digits of two numbers and if one sum found to be greater then print that number to the stdout. If found both sum to be equal then print 'Equal' to the stdout.

Input Format
Two integer values to be taken as input from stdin. 

Constraints
1 < (a,b) < 10^9

Output Format
Print the single number after comparison. If found equal, then print 'Equal' to the stdout. 

Sample TestCase 1
Input
345678 444444

Output
345678
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def plus(n):
	s = 0
	while n !=0:
		t = n%10
		n = n//10
		s+=t
	return s

def main():

 # Write code here 
 a,b = input().strip().split()
 a,b = int(a),int(b)
 
 a1 = plus(a)
 b1 = plus(b)

 if a1 > b1:
 	stdout.write(str(a))
 elif b1 > a1:
 	stdout.write(str(b))
 else:
 	stdout.write("Equal")

main()

