"""
DAY-2 : Exploring Data Types
For this challenge, you need to read a line from stdin and check whether it is of type integer, float or string.
If input is-
    Integer print 'This input is of type Integer.' to the stdout
    Float print 'This input is of type Float.' to the stdout
    String print 'This input is of type string.' to the stdout
    else print 'This is something else.' to the stdout.

Input Format
A single line to be taken as input as save it to a variable(name of your choice). 

Constraints
1 < |s| < 10000

Output Format
Print the text according to the data type you get as an input
"""
from sys import stdout
import re

def check_type(inp):
	float_pattern =re.compile("-?\d+[.]\d+")
	int_pattern = re.compile("-?\d")
	str_pattern = re.compile("\w")
	float_match = float_pattern.match(inp)
	int_match =  int_pattern.match(inp)
	str_match = str_pattern.match(inp)

	print(float_match)
	print(int_match)
	print(str_match)
	if float_match is not None:
		return "f"

	if int_match is not None:
		return "i"

	if str_match is not None:
		return "s"
	
	return "n"

def main():

 # Write code here 
 inp = input()

 if check_type(inp) == "i":
 	print("This input is of type Integer.")
 elif check_type(inp) ==  'f':
 	print('This input is of type Float.')
 elif check_type(inp)  == 's':
 	print('This input is of type string.')
 else:
 	print('This is something else.')

main()