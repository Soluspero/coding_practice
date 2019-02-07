"""
 Identity Matrix (100 Marks)
Numpy Package contains an inbuilt tool named identity
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0.
You have to print a numpy array(square matrix of size N*N) consisting of integers with diagonal elements as 1 and rest as 0.

Input Format
First and only line of input contains an Integer N.

Constraints
2 <= N <= 100

Output Format
Output a Identity Matrix of Size N*N.
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def im(n):
    alist=[]
    for v in range(n):
        strr=""
        al =[]
        for i in range(n):
            vl = 1 if i == v else 0
            a = "{:>{w}d}".format(vl,w=1)
            al.append(a)
        st = " ".join(al)
        strr ="["+st+"]"
        alist.append(strr)
    return alist
    
def printim(strlist):
    sys.stdout.write("[")
    for i in range(len(strlist)):
        if i > 0:
            a = "{:>{w}s}".format(strlist[i],w=len(strlist[i])+1)
            sys.stdout.write(a)
        else:
            a = a = "{:>{w}s}".format(strlist[i],w=1)
            sys.stdout.write(a)
        if i < len(strlist)-1:
            sys.stdout.write("\n")
    sys.stdout.write("]")
    
def main():

 # Write code here 
 n = int(input())
 printim(im(n))
 

main()



