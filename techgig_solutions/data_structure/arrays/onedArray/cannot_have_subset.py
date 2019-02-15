''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = list()
 for x in range(n):
     alist.append(int(input().strip()))
     
 sm = 1
 for i in range(n):
     if alist[i]<=sm:
         sm+= alist[i]
     else:
         break
 sys.stdout.write(str(sm))

main()

