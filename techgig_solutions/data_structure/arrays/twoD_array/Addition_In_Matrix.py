from sys import stdout
def main():

 # Write code here 
 row, col = input().strip().split()
 summ =0 

 for r in range(int(row)):
 	for cv in list(map(int,input().strip().split())):
 		summ+=cv

 stdout.write(str(summ))

main()