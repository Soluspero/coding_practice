'''
 Search In A Sorted Array (100 Marks)
Given a sorted array and a number x, find a pair in array whose sum is closest to x and you need to add those two numbers and print that number to the stdout.

Input Format
You will be taking a number as an input from stdin which tells about the length of the array. On another line, array elements should be there with single space between them. Next line should have a integer value. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5
1 < Val < 10^5

Output Format
You need to print the addition of two numbers whose sum is closest to x. 

Sample TestCase 1
Input
6
10 22 28 29 30 40
54
Output
52
Explanation

The two numbers are 22, 30 and their addition is 52.

'''
'''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = list(map(int,input().strip().split()))
	trg = int(input().strip())
	search_list=set()
	b = trg//10

	for x in range(n-1,0,-1):
		for y in range(x):
			if (splist[x]+splist[y])//10 == b or (splist[x]+splist[y]) >=trg:
				search_list.add(splist[x]+splist[y])


	closest = abs(max(search_list)- trg)
	v = 0

	for x in sorted(search_list,reverse=True):
		if abs(x - trg) < closest:
			closest = abs(x - trg)
			v = x


	stdout.write(str(v))


main()

