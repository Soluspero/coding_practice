''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
E D C B A
E D C B A
E D C B A
E D C B A
E D C B A
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n-1,-1,-1):
    s+=chr(65+i)+" "
 
 for i in range(n):
     sys.stdout.write(s.strip())
     if i != n-1:
         sys.stdout.write("\n")
 
main()

