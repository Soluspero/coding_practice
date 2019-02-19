"""
        1
      3 3 3
    5 5 5 5 5
  7 7 7 7 7 7 7
9 9 9 9 9 9 9 9 9
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 
 for i in range(1,2*n,2):
    stdout.write(" "*((2*n-2)-(i-1)))
    for j in range(1,i+1):
        s=(str(j)+" ")*j
    stdout.write(s.strip())
    
    if i < (2*n-2):
        stdout.write("\n")
main()



