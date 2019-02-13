''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = [int(x) for x in input().strip().split()]
 even=sum([alist[x] for x in range(n) if alist[x]%2==0])
 odd = sum([alist[x] for x in range(n) if alist[x]%2!=0])
 
 if even > odd:
    sys.stdout.write("Even")
 elif odd > even:
    sys.stdout.write("Odd")
 else:
    sys.stdout.write("Tied")
 


main()

