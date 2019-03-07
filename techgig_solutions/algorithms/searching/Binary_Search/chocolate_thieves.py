'''
Chocolate Thieves (100 Marks)
Bad news came to Mike's village, some thieves stole a bunch of chocolates from the local factory! Horrible!

Aside from loving sweet things, thieves from this area are known to be very greedy. So after a thief takes his number of chocolates for himself, the next thief will take exactly k times more than the previous one. The value of k (k > 1) is a secret integer known only to them. It is also known that each thief's bag can carry at most n chocolates (if they intend to take more, the deal is cancelled) and that there were exactly four thieves involved.
Sadly, only the thieves know the value of n, but rumours say that the numbers of ways they could have taken the chocolates (for a fixed n, but not fixed k) is m. Two ways are considered different if one of the thieves (they should be numbered in the order they take chocolates) took different number of chocolates in them.
Mike want to track the thieves down, so he wants to know what their bags are and value of n will help him in that. Please find the smallest possible value of n or tell him that the rumors are false and there is no such n.

Input Format
You will be given a function with integer m,  the number of ways the thieves might steal the chocolates, as rumours say as a single argument.

Constraints
1 < = m < = 10^9

Output Format
Return the only integer n  the maximum amount of chocolates that thieves' bags can carry. If there are more than one n satisfying the rumors,return the smallest one.
If there is no such n for a false-rumoured m, return  - 1.
Sample TestCase 1
Input

1

Output

8

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def get_value(a,r):
	return a*r*r*r

def chocolateThieves(number):
	maxList = []
	dupList =[]
	maxx, value, result = 0,0,-1
	for i in range(1,number+1):
		for j in range(2,number+2):
			value = get_value(i,j)
			if len(maxList) >= number:
				maxx = max(maxList)
				if value in maxList:
					dupList.append(value)

				if maxx > value:
					del maxList[maxList.index(maxx)]
					maxList.append(value)
			else:
				maxList.append(value)

	for i in maxList:
		if i in dupList:
			del maxList[dupList.index(i)]

	if maxList != [] and len(maxList) == number:
		result = max(maxList)
	else:
		result = -1

	return result


def main():
	# Write code here 
	n = int(input().strip())
	result = chocolateThieves(n)
	stdout.write(str(result))

main()