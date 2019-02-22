"""
 Persistent Bookcase (100 Marks)
Recently in school Alina has learned what are the persistent data structures: they are data structures that always
 preserves the previous version of itself and access to it when it is modified.
After reaching home Alina decided to invent her own persistent data structure. Inventing didn't take long:
 there is a bookcase right behind her bed. Alina thinks that the bookcase is a good choice for a persistent 
 data structure. Initially the bookcase is empty, thus there is no book at any position at any shelf.
The bookcase consists of n shelves, and each shelf has exactly m positions for books at it. Alina enumerates
 shelves by integers from 1 to n and positions at shelves from 1 to m. Initially the bookcase is empty, thus there is
  no book at any position at any shelf in it.
Alina wrote down q operations, which will be consecutively applied to the bookcase. Each of the operations has 
one of four types:

    1 i j Place a book at position j at shelf i if there is no book at it.
    2 i j Remove the book from position j at shelf i if there is a book at it.
    3 i Invert book placing at shelf i. This means that from every position at shelf i which has a book at it, the book should be removed, and at every position at shelf i which has not book at it, a book should be placed.
    4 k Return the books in the bookcase in a state they were after applying k-th operation. In particular, k = 0 means that the bookcase should be in initial state, thus every book in the bookcase should be removed from its position.

After applying each of operation Alina is interested in the number of books in the bookcase. Alina got 'A' in the school and had no problem finding this values. Will you do so?

Input Format
------------------
The first line of the input contains three integers n, m and q,  the bookcase dimensions and the number of operations respectively.
The next q lines describes operations in chronological order  i-th of them describes i-th operation in one of the four formats described in the statement.
It is guaranteed that shelf indices and position indices are correct, and in each of fourth-type operation the number k corresponds to some operation before it or equals to 0.

Constraints
1 < = n, m < = 10^3
1 < =  q  < = 10^5

Output Format
----------------------
For each operation, print the number of books in the bookcase after applying it in a separate line. The answers should be printed in chronological order.

Sample TestCase 1
Input
4 2 6
3 2
2 2 2
3 3
3 2
2 2 2
3 2

Output
2
1
3
3
2
4
"""
from sys import stdout

def check(row,col, alist):
	count = 0
	for r in range(row):
		for c in range(col):
			if alist[r][c] == 1:
				count+=1
	return str(count)

def do_op(row,col,alist,choice):
	q ,r , c=0,0,-1

	if len(choice) == 2:
		q, r = choice

	if len(choice) == 3:
		q,r,c = choice

	if q == 1 :
		alist[r-1][c-1] = 1

	if q == 2:
		for x in range(r-1,len(alist[r-1])):
			if alist[x][c-1] == 1:
				alist[x][c-1] = 0
				return

	if choice[0] == 3:
		for x in range(r-1,r):
			for c in range(col):
				if alist[x][c] == 0:
					alist[x][c] = 1
				else:
					alist[x][c]= 0


 	# if choice[0] == 4:
 		# pass

def main():

 # Write code here 
 row, col, op=  input().strip().split()
 row, col, op = int(row),int(col), int(op)
 alist = [ [0]*col for x in range(row)]
 
 for r in range(op):
 	choice = list(map(int,input().strip().split()))
 	do_op(row,col,alist,choice)
 	# print(alist)
 	stdout.write(check(row,col,alist))

 	if r < op-1:
 		stdout.write("\n")
 		

main()

     