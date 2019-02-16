''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist = [int(x) for x in input().strip().split()]
    adict = dict()
    for x in alist:
        if x in adict:
            adict[x]+=1
        else:
            adict[x]=1
    
    s = sum({k for k,v in adict.items() if v ==3})
    sys.stdout.write(str(s))

main()

