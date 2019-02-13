''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = list(map(int,input().strip().split()))
 alist = sorted([x for x in alist if x%2==0],reverse=True)
 m = max(alist)
 
 for i in range(len(alist)):
    if m != alist[i]:
        m = alist[i]
        break
 sys.stdout.write(str(m))
 


main()

