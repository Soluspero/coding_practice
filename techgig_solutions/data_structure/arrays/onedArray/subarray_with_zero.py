''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = sorted([int(x) for x in input().strip().split()])
 start = 0
 strr ="No"
 end = 3
 for i in range(n):
    if sum(alist[start:end])==0 and len(alist[start:end])==3:
        strr = "Yes"
        break
    start+=1
    end+=1
 sys.stdout.write(strr)

main()

