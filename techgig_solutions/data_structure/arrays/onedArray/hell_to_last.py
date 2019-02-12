''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist =list()

    for x in range(n):
         alist.append(int(input().strip()))
       
    d = {x:[] for x in set(alist)}
    
    for i,v in enumerate(alist):
    	d[v].append(i)

    d = tuple(x for x in d.items() if len(x[1]) >1)
    mx = max(d[0][1])
    
    if len(d) == 1:
    	sys.stdout.write(str(alist[mx]))
    else:
    	for x in d:
    		if max(x[1]) >= mx :
    			mx = max(x[1])

    	sys.stdout.write(str(alist[mx]))

main()

