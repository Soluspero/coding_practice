'''
 Sorting (100 Marks)
For this challenge, you will be given an array and you are asked to sort the array and print it. 

Input Format
You will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. 

Constraints
1 <= L <= 1000
1 <= Ai <= 1000

Output Format
Print the sorted array to the STDOUT. 

Sample TestCase 1
Input
6
11 9 7 6 12 14
Output
6 7 9 11 12 14

'''

def main():
    n =  6 #int(input().strip())
    splist = [11 ,9 ,7 ,6 ,12, 14] # list(map(int, input().strip().split())

    for i in range(n-1,0,-1):
    	pos = 0
    	for j in range(1,i+1):
    		if splist[j] > splist[pos]:
    			pos = j

    	splist[i], splist[pos] = splist[pos], splist[i]

    print(" ".join(map(str,splist)))

main()