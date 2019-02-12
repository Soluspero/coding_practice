''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist=list(map(int,input().strip().split()))
    s = int(input().strip())
    
    start = 0
    end = 3
    count =0
    for _ in range(n//3):
        v = sum(alist[start:end])
        if v == s:
            count+=1
        start+=end
        end+=3
        
    sys.stdout.write(str(count))

main()

