''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 s =""
 for i in range(1,n+1):
     s+=str(i)+" "
 
 for j in range(n):
 	sys.stdout.write(s.strip())

 	if j != n-1:
 		sys.stdout.write("\n")
 
main()

