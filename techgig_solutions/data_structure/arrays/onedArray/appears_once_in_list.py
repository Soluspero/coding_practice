''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
from collections import Counter
def main():

 # Write code here 
    n  = int(input().strip())
    alist =Counter(list(map(int, input().strip().split())))
    aTuple = tuple(x for x in alist.items())
    res = list(filter(lambda x : x[1]==1, aTuple))
    sys.stdout.write(str(res[0][0]))

main()

