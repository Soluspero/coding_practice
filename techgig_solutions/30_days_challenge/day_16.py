"""
 GCD of two numbers (100 Marks)
For this challenge, you need to take input of two numbers , calculate their greatest common divisor (GCD) and print it to the stdout.

Input Format
You need to take two integers as an input which are separated by a single space. 

Constraints
1 < (a,b) < 10^5

Output Format
Print the single integer result to the stdout. 

Sample TestCase 1
Input
81 81

Output
81

Explanation

81 = 3*3*3*3
81 = 3*3*3*3
so common to both is 3*3*3*3 which is 81
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout
def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

def main():

 # Write code here 
 a,b = input().strip().split()
 a,b = int(a), int(b)
 stdout.write(str(gcd(a,b)))


main()

