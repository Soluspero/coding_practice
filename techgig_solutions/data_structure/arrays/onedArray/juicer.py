''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys
def main():

 # Write code here 
 n ,b,d =  [int(x) for x in input().strip().split()]
 alist = [int(x) for x in input().strip().split()]
 waste=[]
 empty_count=0
 for x in alist:
    if x < b:
        waste.append(x)
    
    if sum(waste) > d:
        empty_count+=1
        waste = []
        
 sys.stdout.write(str(empty_count))
 

main()


