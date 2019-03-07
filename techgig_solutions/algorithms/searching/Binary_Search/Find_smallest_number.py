'''
 Find smallest number (100 Marks)
Find the smallest number with given digit sum s and number of digits d.

Input Format
You will be taking digit sum(s) as an integer on one line and number of digits(d) as integer on another line.

Constraints
1 < = s < = 81
1 < = d < = 9

Output Format
You need to print the output to the stdout.

Sample TestCase 1
Input
9
2
Output
18
Explanation

There are many other possible numbers like 45, 54, 90, etc with sum of digits as 9 and number of digits as 2. The smallest of them is 18
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def bounds(digits):
	upperbound = 10**digits
	lowerbound =0

	if upperbound <=10:
		lowerbound = 0
	else:
		lowerbound = upperbound//10

	return (lowerbound,upperbound)

sd=0
def summ(x, s=0):
	global sd
	sd =s
	if x > 0:
		summ(x//10, s+(x%10))


def main():
	# Write code here 
	trg = int(input().strip())
	digits = int(input().strip())
	sum_of_digits=[]
	bound = bounds(digits)

	for x in range(bound[0],bound[1]):
		summ(x)
		# print(sd)
		if trg == sd:
			sum_of_digits.append(x)

	stdout.write(str(min(sum_of_digits)))


# def main():
# 	a= 11 #int(input())
# 	b=3 #int(input())
# 	l=[]
# 	for x in range(b):
# 		l.append(1)

# 	a=a-b
# 	t=b-1
# 	print(l,a, t)
# 	while a>0:
# 		if a>8:
# 			a=a-8
# 			l[t]=9
# 			print("if ", l,a,t)
# 		else:
# 			l[t]=l[t]+a
# 			a=a-a
# 			print("e ", l,a,t)
# 			break
# 		t=t-1

# 	print("".join(list(map(str,l))))


# def main():
#     dsum = int(input())
#     ndigits = int(input())
    
#     nums = list(range(1,10))
    
#     smallest_num = ''
#     flag = 0
#     for n in range(ndigits):
#         smallest_num += "1"
#     iterate = list(range(len(smallest_num)))
#     iterate.reverse()
    
#     for pos in iterate:
#         for n in nums:
#             s = list(smallest_num)
#             s[pos] = str(n)
#             smallest_num = ''.join(s)
#             if sum([int(x) for x in list(smallest_num)]) == dsum:
#                 flag = 1
#                 break
#             if flag == 1:
#                 break
#     print(smallest_num)



main()

