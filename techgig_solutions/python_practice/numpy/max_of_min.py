"""
 Max of Min (100 Marks)
You will be given a 2-Dimensional Matrix of size NxM.
By using Inbuilt Max and Min function present in NumPy Package, You have to perform the min function over axis = 0 and then find the max of that.

Input Format
First line contains two integers N and M, denoting the size of the Matrix.
Next N lines contains M integers.

Constraints
2 <= N <= 100
2 <= M <= 100

Output Format
You have to print an Integer denoting the answer i.e  maximum over minimum(axis = 0)
"""
import sys

def amin(minlist):
	mlist=[]
	for i in minlist:
		mlist.append(min(i))

	return mlist

def transpose(alist,row,col):
	translist=[]
	for ir in range(col):
		ll=[]
		for ic in range(row):
			ll.append(alist[ic][ir])
		translist.append(ll)
	
	return translist
	

def main():
	row,col=input().strip().split()
	alist=[[0] * int(col) for i in range(int(row))]
	minlist=[]

	for ir in range(int(row)):
		for ic,cv in enumerate(list(map(int,input().strip().split()))):
		    alist[ir][ic] = cv
	
	for ir in transpose(alist,int(row),int(col)):
	    minlist.append(ir)
	 
	sys.stdout.write(str((max(amin(minlist)))))

main()