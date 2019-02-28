'''
 Play with digits of a number (100 Marks)
For this challenge, you will take an integer input from stdin, store it in a variable, find the digits in that number, identify digits that are odd and add them, identify which digits are even and add them. Subtract the smaller with the larger one.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Constraints
1 < N < 10^9

Output Format
Print the single number after subtraction. 

Sample TestCase 1
Input
34567

Output
5
Explanation

For the above number, 3,5 and 7 are odd digits and their sum is 15. 4 and 6 are even digits and their sum is 10. Now, subtraction of 10 from 15 results 5 which is your answer. 
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 even, odd =  0,0

 while n !=0:
 	t = n%10
 	n = n//10

 	if t%2 ==  0:
 		even+=t
 	else:
 		odd+=t

 stdout.write(str(abs(even-odd)))

main()