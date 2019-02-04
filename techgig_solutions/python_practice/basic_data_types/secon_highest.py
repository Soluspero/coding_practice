''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def main():

 # Write code here 
 heights  = []
 name_and_height =[]
 n = int(input())
 for _ in range(n):
     name=input()
     height = int(input())
     name_and_height.append((name,height))
     heights.append(height)
     
 heights = sorted(heights,reverse=True)
 name_and_height = sorted(name_and_height)
 
 for n,h in name_and_height:
     if h == heights[1]:
         #sys.stdout.write(n.rstrip()+"\n")
         print(n)

main()

