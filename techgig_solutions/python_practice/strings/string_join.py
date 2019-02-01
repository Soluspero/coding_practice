''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys
def main():

 # Write code here 
 c= input()
 sl=[]
 try:
    while True:
        d = input()
        sl.append(d)
 except:
     pass
 sys.stdout.write(c.join(sl))

main()

