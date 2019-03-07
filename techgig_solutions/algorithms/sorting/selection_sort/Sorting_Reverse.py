'''
 Sorting Reverse (100 Marks)
For this challenge, you will be given an array and you are asked to sort the array in reverse order and print it.

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. 

Constraints
1 <= L <= 1000
1 <= Ai <= 1000

Output Format
Print the reverse sorted array to the STDOUT. 

Sample TestCase 1
Input
6
11 9 7 6 12 14

Output
14 12 11 9 7 6
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout 
def main():
    n =  int(input().strip())
    splist =  list(map(int, input().strip().split()))

    for i in range(n-1,0,-1):
    	pos = 0
    	for j in range(1,i+1):
    		if splist[j] < splist[pos]:
    			pos = j

    	splist[i], splist[pos] = splist[pos], splist[i]

    stdout.write(" ".join(map(str,splist)))

main()
