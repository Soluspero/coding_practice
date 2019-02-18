''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(n,0,-1):
     for j in range(1,i+1):
     	s+=str(j)+" "
     stdout.write(s.strip())
     if i != 1:
     	s=""
     	stdout.write("\n")
 print()
main()

