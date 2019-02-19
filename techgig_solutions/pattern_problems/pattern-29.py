"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())

 for i in range(n,0,-1):
     sys.stdout.write(" "*(((2*n)-(i*2))))
     s =(" *")*i
     sys.stdout.write(s.strip())
     if i != 1:
        sys.stdout.write("\n")
 
main()