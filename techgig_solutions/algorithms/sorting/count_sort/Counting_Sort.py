'''
 Counting Sort (100 Marks)
Given an input array of integers, sort the whole array using counting sort.

Input Format
You will be given an array of integers as argument. 

Constraints
1 < N < 10^5
0 < =  A[i] < = 10^5

Output Format
You need to print the sorted integer array elements separated by space. 

Sample TestCase 1
Input
6
6
1
6
7
3
1
Output
1
1
3
6
6
7

'''
from sys import stdout
def main():
    n =  int(input().strip())
    splist = [int(input().strip()) for _ in range(n)]
    aux_list = [0]*(max(splist)+1)

    for i in splist:
    	if aux_list[i] > 0:
    		aux_list[i] += 1
    	else:
    		aux_list[i] = 1

    for idx, val in enumerate(aux_list):
    	if val > 0:
    		for _ in range(val):
    			stdout.write(str(idx))
    			if idx < len(aux_list)-1:
    				stdout.write("\n")
    # print()

main()