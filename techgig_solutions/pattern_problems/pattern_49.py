"""
9 9 9 9 9 9 9 9 9 
   7 7 7 7 7 7 7   
     5 5 5 5 5     
       3 3 3       
         1 
"""

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 for i in range(2*n-1,-1,-2):
    stdout.write(" "*((2*n-2)-(i-1)))
    for j in range(i+1):
        s=(str(j)+" ")*j
    stdout.write(s.strip())
    
    if i > 1:
        stdout.write("\n")
main()







