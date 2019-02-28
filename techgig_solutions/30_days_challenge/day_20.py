''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdout
def main():

 # Write code here 
 s=""
 for x in range(5):
     s+="* "*5
     stdout.write(s.strip())
     if x < 4:
         stdout.write("\n")
         s=""

main()

