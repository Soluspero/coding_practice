''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist =list(map(int, input().strip().split()))
    
    res = len(list(filter(lambda x : x<0, alist)))
    sys.stdout.write(str(res))

main()

