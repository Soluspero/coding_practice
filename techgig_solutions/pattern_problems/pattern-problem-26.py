''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""
from sys import stdout
def main():

 # Write code here 
  n = int(input().strip())
  s=""
  for i in range(1,n+1):
     stdout.write(" "*(((2*n)-(i*2))))
     for j in range(1,i+1):
         s+= str(j)+" "
     stdout.write(s.strip())
     
     if i < n:
         s=""
         stdout.write("\n")
  # print()
main()