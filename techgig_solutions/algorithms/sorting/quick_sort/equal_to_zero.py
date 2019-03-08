'''
 Equal To Zero (100 Marks)
You will be given an array and you need to find those three elements whose sum are equal to 0. If found print True to the stdout else print False.

Note: The length of the array should not be less than 3.

Input Format
You will be taking a number as an input stdin which tells about the length of the array. On another line, array elements should be there with single space between them.

Constraints
3 <= L <= 1000
1 <= Ai <= 1000

Output Format
You need to print True if found those numbers else print False.

Sample TestCase 1
Input
6
70 69 44 -28 -16 79
Output
True
Explanation

The sum of 44, -28 and -16 equals 0 hence True .

'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def main():
    n =  int(input().strip())
    splist = list(map(int, input().strip().split()))
    start=0
    last = 3
    flag = False

    for x in range(n):
        if sum(splist[start:last])==0:
            flag = True
            break
        start+=1
        last+=1


    stdout.write(str(flag))

main()

main()