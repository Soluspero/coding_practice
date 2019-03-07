'''
 Search Small Ones (100 Marks)
You will be given an array and you need to find the smallest and second smallest numbers and add them.
The length of the array should not be less than 2.
Expected Time Complexity - O(n)

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.

Constraints
2 <= L <= 1000
1 <= Ai <= 1000

Output Format
You need to print the addition of smallest and second smallest element to the stdout.

Sample TestCase 1
Input
7
48 77 7 11 49 99 78
Output
18

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = sorted(set(map(int,input().strip().split())))
    
	stdout.write(str(splist[0]+splist[1]))


main()




