''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
"""

from sys import stdout
def main():

 # Write code here 
  n = int(input().strip())
  for i in range(1,n+1):
     s = (chr(65+i-1)+" ")*n
     stdout.write(s.strip())
     
     if i < n:
         stdout.write("\n")
  print()
main()

