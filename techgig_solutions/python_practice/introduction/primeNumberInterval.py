''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def main():

 # Write code here 
 start = int(input())
 stop = int(input())
 sl=[]
 for num in range(start, stop+1):
     if num > 1:
        for i in range(2,num//2):
            if num%i == 0:
                break
        else:
            #print(num, sep="\n",end="\n",file=sys.stdout, flush=False)
            sl.append(str(num))
 sys.stdout.write("\n".join(sl))
    

main()

