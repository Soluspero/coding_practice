''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
from collections import Counter
def main():

 # Write code here 
    n  = int(input().strip())
    alist = Counter([int(x) for x in input().strip().split()])
    a = alist.most_common(1)
    sys.stdout.write(str(a[0][0] if a[0][1] > n//2 else -1))

main()

