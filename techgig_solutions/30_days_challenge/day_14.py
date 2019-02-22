"""
Lets make a dictionary order
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())
 alist =[]
 for i in range(n):
     alist.append(input().strip())
 
 stdout.write("\n".join(sorted(alist)))

main()

