''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = [int(x) for x in input().strip().split()]
 ll=[]
 
 for i in alist:
    if i%3==0 or i%5==0:
        ll.append(i)
    elif i%3==0 or i%5==0:
        ll.append(i)
 sys.stdout.write(str(len(ll)))

main()

