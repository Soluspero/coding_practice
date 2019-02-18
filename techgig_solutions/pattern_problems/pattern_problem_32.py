''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
E E E E E
  D D D D
    C C C
      B B
       A
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n,0,-1):
     sys.stdout.write(" "*(((2*n)-(i*2))))
     s+=(" "+chr(65+i-1))*i
     sys.stdout.write(s.strip())
     if i != 1:
        s=""
        sys.stdout.write("\n")
 
main()

