''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist =[]
    for x in range(n):
        alist.append(input().strip())
        
    sys.stdout.write(str(len(set(alist))))

main()

