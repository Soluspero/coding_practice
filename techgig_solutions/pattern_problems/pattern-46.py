"""
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 k = 0

 for i in range(1,2*n,2):
    stdout.write(" "*((2*n-2)-(i-1)))

    for j in range(0,i):
        if j<=k:
            s+=(chr(65+j)+" ")
    for m in range(k,0,-1):
        s+=(chr(65+m-1)+" ")
    k+=1
    stdout.write(s.strip())

    if i < 2*(n-1):
    	s=""
    	stdout.write("\n")
 # print()

main()