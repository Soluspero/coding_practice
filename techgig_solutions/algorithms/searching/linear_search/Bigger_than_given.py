'''
 Count Bigger (100 Marks)
You will be given an array and a number and you need to count how many numbers are bigger than this number and print this count to the stdout.

Input Format
You will be taking a number as an input using stdin which tells about the length of the array. On another line, array elements should be there with single space between them. Another line will have the number for which you have to do the comparison.

Constraints
1 <= L <= 1000
1 <= Ai <= 1000

Output Format
Print the count to the stdout.

Sample TestCase 1
Input
5
10 11 12 44 66
22
Output
2
Explanation

There are only two numbers which are greater than 22 that are 44 and 66.
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = list(map(int,input().strip().split()))
	trg = int(input().strip())
    
	stdout.write(str(len([x for x in splist if x > trg])))


main()

