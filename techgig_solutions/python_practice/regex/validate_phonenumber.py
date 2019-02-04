''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import re
import sys
def main():

 # Write code here 
 phonePattern=re.compile(r'(\d)(\d){12}')
 n = int(input())
 results =[]
 for _ in range(n):
     ph_num = input()
     mo = phonePattern.search(ph_num)
     if mo != None:
         if mo.group(1) in ['1','2']:
             results.append("Valid")
         else:
             results.append("Invalid")
     else:
         results.append("Invalid")
 
 sys.stdout.write("\n".join(results))
     

main()

