''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
import itertools

def main():

 # Write code here 
 slist = list(input().rstrip())
 sl = ""
 slist = sorted(slist)
 for s,n in itertools.groupby(slist):
     sl+=str((len(list(n)),s))+" "
 sys.stdout.write(sl.strip())

main()

