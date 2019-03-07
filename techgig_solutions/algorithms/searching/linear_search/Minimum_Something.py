'''
 Minimum Something (100 Marks)
A sorted array is rotated at some unknown point, find the minimum element in it.

Input Format
You will be given an array of integers of size N.

Constraints
1 < N < 10^5
1 < A[i] < 10^5

Output Format
You need to print the minimum element.

Sample TestCase 1
Input
6
5
6
1
2
3
4
Output
1

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = [int(input().strip()) for x in range(n)]

	stdout.write(str(min(splist)))


main()