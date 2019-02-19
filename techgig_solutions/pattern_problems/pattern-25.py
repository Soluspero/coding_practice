''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""
from sys import stdout
def main():

 # Write code here 
  n = int(input().strip())
  s=""
  for i in range(1,n+1):
     stdout.write(" "*(((2*n)-(i*2))))
     s+= (str(i)+" ")*i
     stdout.write(s.strip())
     
     if i < n:
         s=""
         stdout.write("\n")
  print()
main()