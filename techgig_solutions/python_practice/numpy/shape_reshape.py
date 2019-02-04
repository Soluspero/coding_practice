''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
I needed  to write reshape and finddim functions of my own as Techgig platform was not
supported or install numpy module.
Anyone can make this program with the help of numpy module easily.
But it was funny coding and re creating reshape and finddim functions.
"""
import sys
def reshape(r,c,arr):
    alist =[]
    start=0
    stop = c
    width = 2 if max(arr) >= 10 else 1
    
    for v in range(r):
        ll = arr[start:stop]
        strr=""
        al =[]
        for i in ll:
            a = "{:>{w}d}".format(i,w=width)
            al.append(a)
        st = " ".join(al)
        strr ="["+st+"]"
        alist.append(strr)
        start+=c
        stop+=c
    return alist
    
def finddim(nlist):
    n =len(nlist)
    row=0
    col=0
    
    for r in range(2,n+1):
        if n%r==0:
            row=r
            break
    for _ in range(1,n):
        if col != n:
            col+=row
    return (row,(col//row))
    
    
    
def main():

 # Write code here 
 n = list(map(int,input().rstrip().split()))
 width =11 if max(n) >= 10 else 8
 dim=finddim(n)
 strlist=reshape(*dim,n)
#  print(reshape(*dim,n))
 sys.stdout.write("[")
 for i in range(len(strlist)):
     if len(strlist)-1 == i:
         sys.stdout.write("{0:>{w}}".format(strlist[i],w=width))
     else:
         sys.stdout.write("{0:>{w}}".format(strlist[i],w=i*width))
         sys.stdout.write("\n")

 # sys.stdout.write("\n".jstrlistoin(strlist).strip())
 sys.stdout.write("]")

main()

