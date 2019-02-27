"""
 Minimum effort - Maximum output (100 Marks)
For this challenge, Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted.

Input Format
On the first line, you need to take an integer input which will be the length of the array. Another line will have space separated integer values. 

Constraints
1 < n < 10^5
1 < A[i] < 10^5

Output Format
Space separated integer values present in the subarray. 

Sample TestCase 1
Input
13
1 2 4 7 10 11 7 12 3 7 16 18 19

Output
4 7 10 11 7 12 3 7
"""
from sys import stdout

def main():

 # Write code here 
 n = int(input().strip())
 splist = list(map(int,input().strip().split()))
 sort_list = sorted(splist)
 subarray = [-1]*n

 for x in range(n-1):
 	if sort_list[x] != splist[x]:
 		subarray[x] = splist[x]

 	if sort_list[x] == splist[x] and x > 0:
 		if splist[x-1]< splist[x] and splist[x+1] > splist[x]:
 			pass
 		else:
 			subarray[x] = splist[x]
 			
 stdout.write(" ".join(map(str,[x for x in subarray if x != -1])))


main()
