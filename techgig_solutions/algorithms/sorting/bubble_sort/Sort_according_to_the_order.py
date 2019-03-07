''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout

def main():
    n =  5 #int(input().strip())
    splist = [0,23,14,12,9] # list(map(int, input().strip().split()))
    order ="inc" #input().strip()

    for i in range(n-1,0,-1):
    	for j in range(i):
    		if order == "inc":
    			if splist[i] < splist[j]:
    				splist[i], splist[j] = splist[j], splist[i]
    		elif order == "dec":
    			if splist[i] > splist[j]:
    				splist[i], splist[j] = splist[j], splist[i]

    print(splist)

main()