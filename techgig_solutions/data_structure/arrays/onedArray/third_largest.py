''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = sorted([int(x) for x in input().strip().split()],reverse=True)
 sys.stdout.write(str(alist[2]))

main()

