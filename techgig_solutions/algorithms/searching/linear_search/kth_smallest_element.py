'''
 Kth Smallest Element (100 Marks)
Given an array and a number k where k is smaller than size of array, we need to find the k th smallest element in the given array.

Input Format
You will be given an array of integers and integer k.

Constraints
1 < n < 10^5
1 < a[i] < 10^5
1 < k < 10^5

Output Format
You need to print the K th Smallest Element.

Sample TestCase 1
Input

6
7
10
4
3
20
15
3

Output

7

Explanation

3rd Smallest Element is 7.

'''
from sys import stdout
def main():
	n = int(input().strip())
	splist = sorted([int(input().strip()) for x in range(n)])
	trg = int(input().strip())

	if trg < n:
		stdout.write(str(splist[trg-1]))
	else:
		stdout.write('1')


main()