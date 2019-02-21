''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
    
from sys import stdout
def main():

 # Write code here 
 row =  int(input().strip())
 col = int(input().strip())
 count = 0

 for r in range(row):
 	for c in list(map(int,input().strip().split())):
 		if c ==0:
 			count+=1

 stdout.write(str(count))

main()

