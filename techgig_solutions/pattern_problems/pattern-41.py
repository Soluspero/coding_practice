"""
		A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I 
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""

 for i in range(1,2*n,2):
    stdout.write(" "*((2*n-2)-(i-1)))
    for j in range(0,i):
    	s+=(chr(65+j)+" ")
    stdout.write(s.strip())
    
    if i < 2*(n-1):
    	s=""
    	stdout.write("\n")
main()