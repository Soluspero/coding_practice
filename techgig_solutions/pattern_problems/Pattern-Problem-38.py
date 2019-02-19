"""
        A
      C C C
    E E E E E
  G G G G G G G
I I I I I I I I I
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 k = 1
 for i in range(0,2*n,2):
    stdout.write(" "*((2*n-1)-(k)))
    s+=(chr(65+i)+" ")*(k)
    stdout.write(s.strip())
    k+=2
    
    if i < (2*n-2):
    	s=""
    	stdout.write("\n")
main()