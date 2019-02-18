''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
        A
      A B
    A B C
  A B C D
A B C D E
"""
from sys import stdout
def main():

 # Write code here 
  n = int(input().strip())
  s=""
  for i in range(1,n+1):
     stdout.write(" "*(((2*n)-(i*2))))
     for j in range(0,i):
         s+= chr(65+j)+" "
     stdout.write(s.strip())
     
     if i < n:
         s=""
         stdout.write("\n")
  # print()
main()