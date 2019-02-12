''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
from collections import Counter
def main():

 # Write code here 
 n  = int(input().strip())
 adict = Counter([int(x) for x in input().strip().split()])
 sys.stdout.write(str(sum([k for k,v in adict.items() if v > 1])))

main()

