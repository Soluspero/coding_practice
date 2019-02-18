''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5 
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n,0,-1):
     s+=(str(n-i+1)+" ")*i
     sys.stdout.write(s.strip())
     if i != 1:
        s=""
        sys.stdout.write("\n")
 
main()

