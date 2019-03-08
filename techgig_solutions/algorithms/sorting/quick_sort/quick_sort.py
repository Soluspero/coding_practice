'''
 Quick Sort (100 Marks)
Given an input array of integers, sort the whole array using Quick Sort.

Input Format
You will be given an array of integers of size N. 

Constraints
1 < N < 10^5
1 < A[i] < 10^6

Output Format
You need to print sorted integer array elements separated by space. 

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
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout 
def quick_sort(splist , first, last):
	if first < last :
		split_point = partition(splist,first,last)

		quick_sort(splist, first, split_point-1)
		quick_sort(splist, split_point + 1, last)

def partition(splist, first, last):
	pivot_value = splist[first]
	left_mark = first + 1
	right_mark = last
	flag = True

	while flag:
		while left_mark<= right_mark and splist[left_mark]<= pivot_value:
			left_mark += 1

		while splist[right_mark]>= pivot_value and right_mark>=left_mark:
			right_mark -= 1

		if right_mark < left_mark:
			flag= False
		else:
			splist[left_mark], splist[right_mark] = splist[right_mark],splist[left_mark]

	splist[first],splist[right_mark] = splist[right_mark],splist[first]

	return right_mark


def main():
    n =  int(input().strip())
    splist =  [int(input().strip()) for _ in range(n)]
    quick_sort(splist, 0 , n-1)

    stdout.write("\n".join(map(str,splist)))

main()