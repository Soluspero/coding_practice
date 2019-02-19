''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
from sys import stdout
def main():
 # Write code here 
 n = int(input().strip())
 k = 2*n-1
 for i in range(2*n,0,-2):
    stdout.write(" "*((2*n-1)-(k)))
    s =("* ")*(k)
    stdout.write(s.strip())
    k-=2
    
    if k > 0 :
    	stdout.write("\n")
main()



