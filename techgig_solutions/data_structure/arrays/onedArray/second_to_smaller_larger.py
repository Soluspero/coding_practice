''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = [int(x) for x in input().strip().split()]
 second_lrg=sorted(alist,reverse=True)[1]
 second_sml=sorted(alist)[1]
 sys.stdout.write(str(second_lrg+second_sml))

main()

