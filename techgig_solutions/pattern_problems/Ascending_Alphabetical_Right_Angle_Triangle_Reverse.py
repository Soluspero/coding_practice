''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
A B C D E
A B C D
A B C
A B
A 
"""
import sys
def main():

 # Write code here 
 n = 5 #int(input().strip())
 s =""
 for i in range(n):
     for j in range(0,n-i):
     	s+=(" "+chr(65+j))
     sys.stdout.write(s.strip())
     if i != n-1:
        s=""
        sys.stdout.write("\n")
 print()
main()

