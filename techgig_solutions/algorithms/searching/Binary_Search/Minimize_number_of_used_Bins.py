'''
 Minimize number of used Bins (100 Marks)
Given n items of different weights and bins each of capacity c, assign each item to a bin such that number of total used bins is minimized. It may be assumed that all items have weights smaller than bin capacity.

Input Format
You will be taking a number as an input from stdin which tells about the length of the array which determines the weights. On another line, array elements should be there with single space between them. Next line should have a integer value which determines the bin capacity.

Constraints
1 < N < 10^5
1 < A[i] < 10^5
1 < Capacity < 10^9

Output Format
You need to print minimum number of bins used.

Sample TestCase 1
Input
6
4 8 1 4 2 1
10
Output
2
Explanation

We need minimum 2 bins to accommodate all items. First bin contains {4, 4, 2} and second bin {8, 2}
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def main():
    n =  int(input().strip())
    splist = list(map(int, input().strip().split()))
    capacity = int(input().strip())

    try:
    	stdout.write(str(sum(splist)//capacity))
    except:
    	stdout.write(str(sum(splist)//capacity +1 ))


main()