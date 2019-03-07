'''
 First repeating element (80 Marks)
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest. 

Input Format
You will be given a function with an integer array as arguments. 

Constraints
1 < N < 10^5
1 < a[i] < 10^5

Output Format
You need to return the first repeating element from the function. 
Sample TestCase 1
Input
7
10
5
3
4
3
5
6
Output
5

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = [int(input().strip()) for x in range(n)]
	start = 1
	repeated = splist[0]
	flag = False

	while start!=n:
		for x in splist[start:]:
			if repeated == x:
				flag = True
				break

		if flag is True:
			break

		repeated = splist[start]
		start+=1

	stdout.write(str(repeated))

main()
