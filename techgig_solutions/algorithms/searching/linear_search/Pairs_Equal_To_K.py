'''
 Pairs Equal To K (100 Marks)
Given an integer array and a positive integer k, count all distinct pairs with difference equal to k.

Input Format
You will be given an integer array of size N and an integer k. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5
1 < k < 10^5

Output Format
You need to print the count of pairs.

Sample TestCase 1
Input
5
1
5
3
4
2
3
Output
2
Explanation

There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2}. 
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 splist = [int(input().strip()) for _ in range(n)]
 trg = int(input().strip())
 count = 0

 for x in range(n-1,0,-1):
     for y in range(x):
         if abs(splist[x]-splist[y]) == trg:
             count += 1

 stdout.write(str(count))

main()

