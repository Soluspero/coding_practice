''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = [int(x) for x in input().strip().split()]
 sys.stdout.write(" ".join(list(map(str,filter(lambda x: x%10!=0,alist)))))
 

main()


