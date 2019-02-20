"""
        A 
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
"""
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
 	s = [chr(65+abs(x-m)) for x in l]
 	stdout.write(chr(65)+" " if m == 0 else " ".join(s))
 	
 	if i < (2*n-2):
 	    l=[]
 	    stdout.write("\n")
 	
main()