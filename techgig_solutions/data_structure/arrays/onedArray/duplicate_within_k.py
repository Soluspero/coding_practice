''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist=list()
    for x in range(n):
        alist.append(int(input().strip()))
        
    k = int(input().strip())
    adict = {i:[] for i in set(alist)}
    for i,v  in enumerate(alist):
        adict[v].append(i)
        
    aTuple = tuple( i for i in adict.items())
    flag = False
    for x in aTuple:
        if len(x[1])==1:
            flag = False
        else:
            diff = x[1][-1]-x[1][0]
            if diff<k:
                flag = True
            else:
                flag = False
            
        
    
    if flag is True:
        sys.stdout.write(str(1))
    else:
        sys.stdout.write(str(0))

main()

