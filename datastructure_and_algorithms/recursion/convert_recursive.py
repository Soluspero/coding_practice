from sys import stdout



# Iterative method to convert binary to decimal.
def convert(n,b):
	p= 0
	s = 0
	while n != 0:
		r = n % 10
		n = n // 10
		s+=r*b**p
		p+=1

	return s

#Recursive method to convert binary to decimal.
result = 0  # Global variable to store result.

def convert_recursive(numsp,b,i=0,s=0):
	global result
	result = s
	if numsp > 0:
		r = numsp%10
		convert_recursive(numsp//10,b,i+1,s+r*b**i)

	return result

# Closure recursive method  to convert binary to decimal
def convert_recursive_closure(numsp,b):
	rs=  0
	def res(numsp,b,i=0,s=0):
		nonlocal rs
		rs = s
		if numsp > 0:
			r = numsp%10
			res(numsp//10,b,i+1,s+r*b**i)

		return rs

	rs = res(numsp,b)

	return rs

def main():

 # Write code here 
 numsp = int(input().strip())
 print(convert(numsp,2))
 print(convert_recursive(numsp,2))
 print(convert_recursive_closure(numsp,2))


main()