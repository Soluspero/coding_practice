''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 Q = int(input())
 ll =[]
 for _ in range(Q):
     qlines =input().split()
     if int(qlines[0]) == 1:
         for i in qlines[1:]:
             ll.append(i)
     elif int(qlines[0]) == 2:
         sys.stdout.write(str(ll)+"\n")

main()

