''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def main():

 # Write code here 
 heights  = set()
 name_and_height =[] 
 n = int(input())
 for _ in range(n):
     name=input()
     height = int(input())
     name_and_height.append((name,height))
     heights.add(height)
     
 heights = sorted(heights,reverse=True)
 name_and_height = sorted(name_and_height)
 ll = []
 for n,h in name_and_height:
     if h == heights[1]:
         ll.append(n.strip())
 sys.stdout.write("\n".join(ll))

main()

