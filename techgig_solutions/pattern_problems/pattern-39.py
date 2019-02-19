"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
"""

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 k = 1
 for i in range(1,n+1):
    stdout.write(" "*((2*n)-(k+i)))
    for j in range(1,k+i):
        s+=(str(j)+" ")
    k+=1
    stdout.write(s.strip())
    
    if i < n:
    	s=""
    	stdout.write("\n")
main()
