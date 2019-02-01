''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here
 str1 = input()
 str2 = input()
 edit =abs(len(str1)-len(str2))

 str1Set = set(str1)
 str2Set = set(str2)

 if len(str1) < len(str2):
 	edit+=len(str1Set.difference(str2Set))
 else:
 	edit = len(str1Set.difference(str2Set))

 sys.stdout.write(str(edit))

main()

