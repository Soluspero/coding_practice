''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

 # Write code here 
 	# n = 5
    n  = int(input().strip())
    alist = [int(x) for x in input().strip().split()]
    # alist = [-1, -2, -3, 4, 10]
    aset = set()
    
    for i in range(n):
    	for j  in range(n-1,0,-1):
    		if i!=j:
    			aset.add((alist[i]-alist[j]-i+j))
    			# print(f"i : {i}, j : {j}, ({alist[i]}-{i})-({alist[j]}-{j}) = {(alist[i]-i)-(alist[j]-j)}")
    	# print()
    sys.stdout.write(str(max(aset)))
    # print()

main()

