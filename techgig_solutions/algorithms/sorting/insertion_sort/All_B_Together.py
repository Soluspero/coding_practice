'''
All B Together (100 Marks)
Given an input string with duplicate characters generate a string which does have all B's together in the front and other characters maintain their respective position.

Input Format
You will be given a string S.

Constraints
1 < |S| < 10^5

Output Format
You need to print the modified string.

Sample TestCase 1
Input

ababacada

Output

bbaaacada
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout 
def main():
    splist =  input().strip()

    all_b=[]
    none_b=[]

    for i in splist:
        if i == 'b' or i == 'B':
            all_b.append(i)
        else:
            none_b.append(i)
    
    splist = all_b+ none_b

    stdout.write("".join(splist))

main()
