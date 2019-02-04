''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
import itertools

def main():

 # Write code here 
 alist = [int(x) for x in input().rstrip().split()]
 blist = [int(x) for x in input().rstrip().split()]
 sl = ""
 
 for s in itertools.product(alist,blist):
     sl+=str(s)+" "
 sys.stdout.write(sl.strip())

main()

