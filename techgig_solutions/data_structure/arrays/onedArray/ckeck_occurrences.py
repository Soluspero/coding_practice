''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
from collections import Counter
def main():

 # Write code here 
    n  = int(input().strip())
    alist = Counter([int(x) for x in input().strip().split()])
    alist = [k for k,v in alist.items() if v == 3 ]
    
    sys.stdout.write('True' if len(alist)>0 else 'False')

main()

