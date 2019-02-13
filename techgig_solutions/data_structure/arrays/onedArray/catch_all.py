''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n1  = int(input().strip())
 alist = set(map(int,input().strip().split()))
 n2  = int(input().strip())
 blist = set(map(int,input().strip().split()))
 n3  = int(input().strip())
 clist = set(map(int,input().strip().split()))
 
 x = ((alist & blist) & clist)
 sys.stdout.write(str(sum(x)))
 


main()

