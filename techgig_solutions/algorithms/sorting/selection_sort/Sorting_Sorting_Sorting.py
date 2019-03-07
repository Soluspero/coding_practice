'''
 Sorting Sorting Sorting (100 Marks)
For this challenge, you will be given an array and you are asked to find multiples of 5 in the given array, sort and put them first in the array. Rest all the elements will preserve their orders.  

Input Format
you will be taking a number as an input from STDIN which tells about the length of the array. On another line, array elements should be there with single space between them. 

Constraints
1 <= L <= 1000
1 <= Ai <= 1000

Output Format
print the required array to the STDOUT. 

Sample TestCase 1
Input
6
9 14 15 10 8 5
Output
5 10 15 9 14 8

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout 
def main():
    n =  int(input().strip())
    splist =  list(map(int, input().strip().split()))

    five=[]
    non_five=[]

    for i in splist:
        if i%5 ==0:
            five.append(i)
        else:
            non_five.append(i)
    
    splist = sorted(five)+non_five
    # print(five, non_five)

    stdout.write(" ".join(map(str,splist)))

main()