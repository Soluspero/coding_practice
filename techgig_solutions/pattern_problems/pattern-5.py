''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n):
    s+=chr(65+i)+" "
 
 for i in range(n):
     sys.stdout.write(s.strip())
     if i != n-1:
         sys.stdout.write("\n")
 
main()

