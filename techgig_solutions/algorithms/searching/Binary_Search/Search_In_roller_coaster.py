'''
 Search In roller coaster (100 Marks)
Given an array of size n, Search if the given  element in array exists such that it is  first increasing then decreasing then increasing or other way round.

Input Format
You will be given an array of integers and a element X. 

Constraints
1 < n < 10^5
1 < a[i] < 10^5
1 < X < 10^5


Output Format
You need to Print 'Yes' if it is present, 'No' otherwise.

Sample TestCase 1
Input
7
7 10 8 5 2 3 5
10
Output
Yes

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def binary_search(splist, trg):

	if len(splist) == 0:
		return False
	else:
		mid = len(splist)//2

		if splist[mid] == trg:
			return True
		else:
			if trg < splist[mid]:
				return binary_search(splist[:mid],trg)
			else:
				return binary_search(splist[mid+1:], trg)
 


def main():
    n =  int(input().strip())
    splist = sorted(list(map(int, input().strip().split())))
    trg = int(input().strip())
    
    if binary_search(splist, trg) is True:
        stdout.write("Yes")
    else:
        stdout.write("No")


main()