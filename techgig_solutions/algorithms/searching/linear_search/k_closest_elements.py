'''
 k closest elements (100 Marks)
Given a sorted array arr[] of N Elements and values k,X, find the k closest elements to X in arr[].

Input Format
You will be given an array of integers and integers k,x as arguments. 

Constraints
1 < N < 10^5
1 < arr[i] < 10^5
1 < k < 100
1 < X < 10^5

Output Format
You need to return the addition of k-closest elements from the given function. 

Sample TestCase 1
Input
13
12
16
22
30
35
39
42
45
48
50
53
55
56
4
35
Output
156

Explanation

4 elements that are closest to 35 are 30,39,42 and 45
156 = 30+39+42+45
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
	n = int(input().strip())
	splist = sorted([int(input().strip()) for x in range(n)])
	k = int(input().strip())
	trg = int(input().strip())
	# n,k,trg = 13,4,35
	# splist = [12,16,22,30,35,39,42,45,48,50,53,55,56]
	closest=[]

	while k > 0:
		for x in splist:
			if x < trg and x//10 == trg//10:
				closest.append(x)
				k-=1

			if x > trg:
				closest.append(x)
				k-=1


	stdout.write(str(sum(closest[:k])))


main()


