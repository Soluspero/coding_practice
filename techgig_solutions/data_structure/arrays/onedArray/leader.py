''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    l =list(map(int, input().strip().split()))
    f = []
    pos =l[-1]
    f.append(pos)
    s = n-1
    for x in range(s,0,-1):
        if l[x-1] >= pos:
            pos = l[x-1]
            s = x-1
            f.append(l[x-1])
    
    sys.stdout.write("\n".join(map(str,sorted(f,reverse=True))))

main()

