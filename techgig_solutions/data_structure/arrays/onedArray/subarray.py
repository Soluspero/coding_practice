''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n = int(input().strip())
 alist = []
 ll = []
 
 for _ in range(n):
    alist.append(int(input().strip()))
    
 for i in range(n-1):
    ll.append(abs(alist[i]-alist[i+1]))
    
 ll = sorted(ll)
 count = 1
 for i in range(len(ll)-1):
    if ll[i+1]-ll[i] == 1:
        count+=1
 sys.stdout.write(str(count))

main()

