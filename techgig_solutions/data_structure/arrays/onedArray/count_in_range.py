''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = list(map(int,input().strip().split()))
 start, end = list(map(int,input().strip().split()))
 x = len([alist[x] for x in range(n) if alist[x]>=start and alist[x]<=end])
    
 sys.stdout.write(str(x))
 


main()

