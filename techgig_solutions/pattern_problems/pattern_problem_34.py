''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 for i in range(1,2*n,2):
    stdout.write(" "*((2*n-2)-(i-1)))
    for j in range(1,i+1):
        s=("* ")*j
    stdout.write(s.strip())
    
    if i < 2*(n-1):
        stdout.write("\n")
main()

