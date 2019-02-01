''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from collections import Counter
import sys

def main():
 # Write code here 
 s = input()
 sl = ""
 for i in Counter(s).most_common(2):
    sl+= str(i) + " "
 sys.stdout.write(sl.strip())

main()

