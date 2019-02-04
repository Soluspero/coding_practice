''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import re
import sys
def main():

 # Write code here 
 cardPattern=re.compile(r'(\d)(\d){3}-?(\d){4}-?(\d){4}-?(\d){4}')
 n = int(input())
 results =[]
 for _ in range(n):
     card_num = input()
     mo = cardPattern.search(card_num)
     if mo != None:
         if mo.group(1) in ['7','8','9']:
             results.append("Valid")
         else:
             results.append("Invalid")
     else:
         results.append("Invalid")
 
 sys.stdout.write("\n".join(results))
     

main()

