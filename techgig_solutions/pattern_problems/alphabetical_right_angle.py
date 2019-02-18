''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
A
B B
C C C
D D D D
E E E E E
"""
from sys import stdout
def main():

 # Write code here 
  n = int(input().strip())
  if n >= 1 and n<=26: 
      for i in range(1,n+1):
         s = (chr(65+i-1)+" ")*i
         stdout.write(s.strip())
         
         if i < n:
             stdout.write("\n")
#   print()
main()

