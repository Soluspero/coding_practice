"""
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())

 for i in range(n,0,-1):
     sys.stdout.write(" "*(((2*n)-(i*2))))
     s =(" "+str(i))*i
     sys.stdout.write(s.strip())
     if i != 1:
        sys.stdout.write("\n")
 
main()