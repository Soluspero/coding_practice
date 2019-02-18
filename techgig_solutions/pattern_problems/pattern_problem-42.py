''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
        A
      C B A
    E D C B A
  G F E D C B A
I H G F E D C B A
"""

import sys
def main():

 # Write code here 
 n = 5 #int(input().strip())
 for i in range(n,0,-1):
 	for j in range(1,i):
 		print(" ",end="")

 	for k in range(n ,i,-1):
 		print(" *",end="")
 	print(" ")
main()

