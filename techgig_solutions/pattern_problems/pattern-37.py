"""
        A
      B B B
    C C C C C
  D D D D D D D
E E E E E E E E E
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 k = 1
 for i in range(0,n):
    stdout.write(" "*((2*n-1)-(k)))
    s+=(chr(65+i)+" ")*(k)
    stdout.write(s.strip())
    k+=2
    
    if i < n-1:
    	s=""
    	stdout.write("\n")
main()