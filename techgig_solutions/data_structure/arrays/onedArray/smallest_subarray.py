''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
    n  = 6 #int(input().strip())
    alist = [1, 4, 45, 6, 0, 19] #[1, 10,5,2,7] #[int(x) for x in input().strip().split()]
    trg = 51 #int(input().strip())
    mx = alist[0]
    mn = n+1

    if mx > trg:
        sys.stdout.write(str(len(alist[0])))
    else:
        start=0
        # mn = n+1
        while start!=n:
            mx  = alist[start]
            count = 0
            for x in range(start,n):
                # print("bf ","x ",x,",start ",start,", mx",mx,",mn ",mn,", count",count,(mx > trg) and (count < mn))
                mx += alist[x]
                count+=1
                print("af ","x ",x,",start ",start,", mx",mx,",mn ",mn,", count",count,(mx > trg) and (count < mn))

                if mx > trg:
                    if count < mn:
                        print(mn,count)
                        mn = count
                        # count = 0
                        print("mn ",mn,", count",count)
            start+=1
        sys.stdout.write(str(mn))

    print()

main()

