''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
from collections import namedtuple
def main():

 # Write code here 
 studlist =[]
 marks=[]
 n = int(input())
 headings = input().rstrip().split()
 Student = namedtuple("Student",headings)
 for _ in range(n):
 	headings = input().rstrip().split()
 	studlist.append(Student(*headings))

 for stud in studlist:
    marks.append(int(stud.marks))
 
 avg ="{:.2f}".format( (sum(marks)/(n*100))*100)
 sys.stdout.write(avg)

main()

