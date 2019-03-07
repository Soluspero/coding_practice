'''
 Binary Search (100 Marks)
Given an array of numbers of size n and integer x. Search whether x is present in array or not. If yes, return true else return false. You need to perform binary search on the given array. 

Input Format
You will be given an array of Integers and An Integer X.

Constraints
1 < N < 10^5
1 < A[i] < 10^5
1 < X < 10^5

Output Format
You need to Print 'Yes' if the X is present in the array and 'No' otherwise.

Sample TestCase 1
Input
5
1
12
22
32
42
12
Output
Yes

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def binary_search(splist, first, last, trg):
	n = len(splist)

	for x in range(n):
		mid = (first+last)//2

		if splist[mid] == trg:
			return True
		else:
			if trg < splist[mid]:
				last = mid - 1
			else:
				first = mid + 1

	return False



def main():

 # Write code here 
 n = int(input().strip())
 splist = [int(input().strip()) for _ in range(n)]
 trg = int(input().strip())

 stdout.write("Yes" if binary_search(splist,0, n-1,trg) else "No")
main()

