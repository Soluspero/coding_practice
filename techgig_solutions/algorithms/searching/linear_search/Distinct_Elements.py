'''
 Distinct Elements (100 Marks)
Given an integer array, print all distinct elements in array. The given array may contain duplicates and the output should print every element only once. The given array is not sorted.

Input Format
You will be given an integer array of size N.

Constraints
1 < N < 10^5
1 < A[i] < 10^6

Output Format
You need to print array of distinct elements.

Sample TestCase 1
Input
8
12
10
9
45
2
10
10
4
Output
12
10
9
45
2
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
    n = int(input().strip())
    splist =[]
    for x in range(n):
        x = input().strip()
        if x not in splist:
            splist.append(x)
    
    stdout.write("\n".join(splist))

main()