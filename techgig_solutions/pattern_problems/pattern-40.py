"""
        1
      3 2 1
    5 4 3 2 1
  7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 k = 0
 for i in range(1,n+1):
    stdout.write(" "*((2*n-1)-(k+i)))
    for j in range(k+i,0,-1):
        s+=(str(j)+" ")
    k+=1
    stdout.write(s.strip())
    
    if k < n:
        s=""
        stdout.write("\n")
main()
