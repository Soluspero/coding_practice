''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
"""

from sys import stdout
def main():

 # Write code here 
  n = int(input().strip())
  for i in range(n,0,-1):
     s = (chr(65+i-1)+" ")*n
     stdout.write(s.strip())
     
     if i != 1:
         stdout.write("\n")
main()


