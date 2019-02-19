"""
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 k=2*n-1
 
 for i in range(n,0,-1):
    stdout.write(" "*((2*n-1)-(k)))
    s=(str(i)+" ")*k
    k-=2
    stdout.write(s.strip())
    
    if i > 1:
        stdout.write("\n")
main()
