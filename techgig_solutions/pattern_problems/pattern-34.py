''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
A B C D E
  A B C D
    A B C
      A B
        A
"""

import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n,0,-1):
     sys.stdout.write(" "*(((2*n)-(i*2))))
     for j in range(i):
        s+=" "+chr(65+j)
     sys.stdout.write(s.strip())
     if i != 1:
         s=""
         sys.stdout.write("\n")
 
main()