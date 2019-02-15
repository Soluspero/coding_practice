''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = []
 for x in range(n):
     alist.append(int(input().strip()))

 c = []     
 maxx = max(alist)
 for x in range(n):
     if alist[x]<maxx:
         c.append(maxx-alist[x])
 
#  print(c)
         
 sys.stdout.write(str(sum(c)))

main()



