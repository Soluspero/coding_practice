''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
A A A A A
B B B B
C C C
D D
E
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n):
     # sys.stdout.write(" "*(((2*n)-(i*2))))
     s+=(" "+chr(65+i))*(n-i)
     sys.stdout.write(s.strip())
     if i != n-1:
        s=""
        sys.stdout.write("\n")
 
main()

