''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
output
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
import sys
def main():

 # Write code here 
 n = int(input().strip())
 for i in range(1,n+1):
     s = ("*"+" ")*(n-1)
     sys.stdout.write(s.strip())
     if i < n:
         sys.stdout.write("\n")
 
main()

