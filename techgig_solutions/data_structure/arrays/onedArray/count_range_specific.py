''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
'''
 Count In Range And Specific (100 Marks)
You will be given an array and a range and you need to count how many array 
elements lies in that range and not divisible by 3 and 5.

Input Format
First line will contain an Integer indicating size of the array.
Next line will contain n integer denoting the array elements.

Constraints
1 <= L <= 1000
1 <= Ai <= 1000

Output Format
Print the count to the STDOUT. 

Sample TestCase 1
Input
6
16 17 4 3 5 2
2 10

output
2
'''
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = [int(x) for x in input().strip().split()]
 start,stop = [int(x) for x in input().strip().split()]
 alist =list(filter(lambda x: x>=start and x<=stop,alist))
 sys.stdout.write(str(len(list(filter(lambda x: x%3!=0 and x%5!=0,alist)))))
 

main()

