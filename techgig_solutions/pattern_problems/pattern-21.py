''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(1,n+1):
     for j in range(n,i-1,-1):
     	s+=str(j)+" "
     stdout.write(s.strip())
     if i != n:
     	s=""
     	stdout.write("\n")
 # print()
main()

