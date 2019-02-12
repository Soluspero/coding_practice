''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist = [int(x) for x in input().strip().split()]
    
    res = [str(x) for x in alist if x%2==0]
    sys.stdout.write("".join(res) if len(res)>0 else '0')

main()

