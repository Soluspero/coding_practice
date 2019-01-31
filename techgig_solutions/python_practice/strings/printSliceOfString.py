''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys

def main():

 # Write code here 
 s = input()
 start = int(input())
 stop = int(input())
 #print(s[start:stop+1],file=sys.stdout)
 sys.stdout.write(s[start:stop+1])

main()

