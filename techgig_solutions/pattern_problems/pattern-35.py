"""
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
"""
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 s=""
 k=1
 for i in range(1,2*n,2):
    stdout.write(" "*((2*n-2)-(i-1)))
    for j in range(1,i+1):
        s=(str(k)+" ")*j 
    k+=1
    stdout.write(s.strip())
    
    if i < 2*(n-1):
        stdout.write("\n")
main()




































# import sys
# def main():

#  # Write code here 
#  n = 5 #int(input().strip())
#  s=""
#  for i in range(1,2*n,2):
#  	for j in range(1,i+1):
#  		s+=(str(j)+" ")
#  	sys.stdout.write("{:^{w}}".format(s.strip(),w=(n*4-1)))
#  	if i < 2*n:
#  		s =""
#  		sys.stdout.write("\n")

#  print()
# main()