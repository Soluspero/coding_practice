''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 s = input()
 sl = s.split(" ")
 flag = False
 for i in sl:
     if i.istitle():
         flag = True
     else:
     	flag = False
 sys.stdout.write(str(flag))
     

main()
