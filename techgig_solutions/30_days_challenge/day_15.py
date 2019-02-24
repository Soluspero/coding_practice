"""
Day 15 : Calculate power using Recursion
This program takes two integers from user ( base number and a exponent) and calculates the power. Instead of using loops to calculate power, this program uses recursion to calculate the power of a number.

Input Format
For this challenge, you need to take 2 integer inputs from stdin which are separated by a single space. 

Constraints
1 < N < 50
0 <= P <= 12

Output Format
You will print the answer to the stdout. 

Sample TestCase 1
Input
4 3

Output
64

Explanation

4^3 = 4*4*4 = 64 
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def recursive_power(b,e):
	if e == 0 :
		return 1
	elif e == 1:
		return b
	else:
		return b * recursive_power(b,e-1)

def main():

 # Write code here 
 b, e = input().strip().split()
 # stdout.write(str(int(b)**int(e)))
 print(recursive_power(int(b),int(e)))

main()

