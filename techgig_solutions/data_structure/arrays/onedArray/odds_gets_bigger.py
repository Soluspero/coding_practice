''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist = [int(x) for x in input().strip().split()]
    a = sorted([str(x) for x in alist if x%2!=0],reverse=True)
    sys.stdout.write("".join(a) if len(a) > 0 else str(0))

main()

