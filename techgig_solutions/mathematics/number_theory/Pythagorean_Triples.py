'''
 Pythagorean Triples (100 Marks)
Katya studies in a fifth grade. Recently her class studied right triangles and the Pythagorean theorem. It appeared, that there are triples of positive integers such that you can construct a right triangle with segments of lengths corresponding to triple. Such triples are called Pythagorean triples.
For example, triples (3, 4, 5), (5, 12, 13) and (6, 8, 10) are Pythagorean triples.
Here Katya wondered if she can specify the length of some side of right triangle and find any Pythagorean triple corresponding to such length? Note that the side which length is specified can be a cathetus as well as hypotenuse.
Katya had no problems with completing this task. Will you do the same?

Input Format
The only line of the input contains single integer n, the length of some side of a right triangle.

Constraints
1 <= n <= 10^9
1 <= m, k <= 10^18


Output Format
Print two integers m and k, such that n, m and k form a Pythagorean triple, in the only line.
In case if there is no any Pythagorean triple containing integer n, print - 1 in the only line. If there are many answers, print any of them.
Sample TestCase 1

Input
3

Output
4 5
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from sys import stdout
def main():

 # Write code here 
 n = int(input().strip())

 if n%2 == 0:
 	stdout.write(str((n//2)**2 -1) + " " + str((n//2)**2 + 1))


 if n%2 != 0:
 	stdout.write(str((n**2-1)//2) + " " + str((n**2 + 1)//2))


main()

