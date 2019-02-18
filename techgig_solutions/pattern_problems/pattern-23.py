"""
E D C B A
E D C B
E D C
E D
E 
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n-1,-1,-1):
     for j in range(n-1,n-i-2,-1):
     	s += (" "+chr(65+j))
     sys.stdout.write(s.strip())
     if i > 0:
        s=""
        sys.stdout.write("\n")
 # print()
 
main()