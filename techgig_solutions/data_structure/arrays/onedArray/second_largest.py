''' 
 Second largest (100 Marks)
You will be given 4 numbers one on each line and you are asked to find the second largest number and print them to the STDOUT . 

Input Format
You will take 4 integers as input from STDIN. 

Constraints
1<= Integer values <= 1000

Output Format
print your result which will be the integer only to the STDOUT. 

sample input
4567
9876
345
12

output
345
'''
import sys
def main():

 # Write code here 
 n  = 4
 alist = []
 for x in range(n):
     a = int(input().strip())
     if a>=1 and a<=1000:
         alist.append(a)
     

 sys.stdout.write(str(max(alist)))

main()
