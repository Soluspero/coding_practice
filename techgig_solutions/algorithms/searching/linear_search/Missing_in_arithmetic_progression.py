'''
 Missing in arithmetic progression (100 Marks)
Given an arithmetic progression with one number missing find that missing number. 

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5

Output Format
You need to print the missing number to the STDOUT. 

Sample TestCase 1
Input
7
1 7 10 13 16 19 22
Output
4

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
from collections import Counter

def find_diff(splist,n):
    for x in range(n-1):
        yield abs(splist[x+1]-splist[x])

def main():
    n = int(input().strip())
    splist = list(map(int,input().strip().split()))
    
    diff = Counter(list(find_diff(splist,n))).most_common(1)[0][0]

    for x in range(n-1):
        if abs(splist[x+1]-splist[x]) != diff:
            stdout.write(str(splist[x]+diff))
            break


main()