''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def main():

 # Write code here 
 start = 900
 stop = 1000
 
 for num in range(start, stop+1):
     if num > 1:
        for i in range(2,num//2):
            if num%i == 0:
                break
        else:
            print(num, file=sys.stdout, flush=False)

 print("a","b",sep="\n")

main()

