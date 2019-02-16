''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = int(input().strip())
    alist = sorted([int(x) for x in input().strip().split()],reverse=True)
    trg = int(input().strip())
    mx = max(alist)
    s =set([mx])
    
    if mx > trg:
        sys.stdout.write(str(len(s)))
    else:
        start=1
        end =3
        for x in range(n):
            sm = mx + sum(alist[start:end])
            if sm > trg:
                for i in alist[start:end]:
                    s.add(i)
                break
            start+=1
            end+=1
    
    sys.stdout.write(str(len(s)))

main()