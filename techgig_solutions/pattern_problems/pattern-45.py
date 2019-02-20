"""
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 k = 1

 for i in range(1,2*n,2):
    stdout.write(" "*((2*n-2)-(i-1)))

    for j in range(1,i+1):
        if j<=k:
            s+=(str(j)+" ")
    for m in range(k-1,0,-1):
        s+=(str(m)+" ")
    k+=1
    stdout.write(s.strip())

    if i < 2*(n-1):
    	s=""
    	stdout.write("\n")
 # print()

main()