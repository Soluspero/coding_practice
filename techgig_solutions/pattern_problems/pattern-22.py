''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
E E E E E
D D D D
C C C
B B
A
"""
from sys import stdout
def main():

 # Write code here 
  n = int(input().strip())
  if n >= 1 and n<=26: 
      for i in range(n,0,-1):
         s = (chr(65+i-1)+" ")*i
         stdout.write(s.strip())
         
         if i != 1:
             stdout.write("\n")
#   print()
main()

