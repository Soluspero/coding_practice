''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
        A
      C B A
    E D C B A
  G F E D C B A
I H G F E D C B A
"""

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""

 for i in range(1,2*n,2):
    stdout.write(" "*((2*n-2)-(i-1)))
    for j in range(i,0,-1):
    	s+=(chr(64+j)+" ")
    stdout.write(s.strip())
    
    if i < 2*(n-1):
    	s=""
    	stdout.write("\n")
main()



