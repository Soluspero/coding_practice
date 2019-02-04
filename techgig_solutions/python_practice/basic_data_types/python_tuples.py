''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n= int(input())
 ll = input().split()
 x = int(input())
 count = 0
 for i in ll:
     if int(i) == x:
         count +=1
 sys.stdout.write(str(count))

main()

