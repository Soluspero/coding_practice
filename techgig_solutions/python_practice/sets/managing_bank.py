''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def main():

 # Write code here 
 n = int(input())
 acc_nums = input().rstrip().split()
 count =set()
 for i in acc_nums:
     count.add(i)
 sys.stdout.write(str(len(count)))

main()

