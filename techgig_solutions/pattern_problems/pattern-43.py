''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
        0 
      1 0 1
    2 1 0 1 2
  3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():
 # Write code here 
 n = int(input().strip())
 l=[]
 
 for i in range(0,2*n,2):
 	stdout.write(" "*((2*n-2)-(i)))
 	for j in range(i,-1,-1):
 		l.append(j)

 	m = len(l)//2 if len(l)>1 else 0
 	s = [str(abs(x-m)) for x in l]
 	stdout.write("0 " if m == 0 else " ".join(s))
 	
 	if i < (2*n-2):
 	    l=[]
 	    stdout.write("\n")
 	
main()


