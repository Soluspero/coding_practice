"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())

 for i in range(n,0,-1):
     s =(" "+str(i))*i
     stdout.write(s.strip())
     if i != 1:
        stdout.write("\n")
 
main()