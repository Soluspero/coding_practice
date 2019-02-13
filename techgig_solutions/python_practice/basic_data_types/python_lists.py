''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def main():

 # Write code here 
 Q = int(input())
 ll =[]
 strr = ""
 for x in range(Q):
     qlines =list(map(str,input().rstrip().split()))
     if qlines[0] == '1':
             ll.append(qlines[1])
     elif qlines[0] == '2':
         strr+= str(ll)+"\n"
 print(strr.strip(),end="")

main()

