'''
 Reverse String (100 Marks)
Given a string, revese it with the help of stack. Please do not use direct function available in the respective library. 

Input Format
You will be given a function with string as argument.

Constraints
1 <= |S| <= 10^3

Output Format
Return the reverse string from the given function.
Sample TestCase 1
Input
abcde
Output
edcba

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout
def main():

 # Write code here 
 splist = list(input().strip());
 s = "";
 while len(splist)>0:
     s+=splist.pop();

 stdout.write(s.strip());

main()

