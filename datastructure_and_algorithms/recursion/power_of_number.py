"""
Power of a number
Ex:
2^2 = 4
"""

def recursive_power(b,e):
	if e == 0 :
		return 1
	elif e == 1:
		return b
	else:
		return b * recursive_power(b,e-1)

def main():
	print(2**3)
	print(recursive_power(4,3))

if __name__ == '__main__':
	main()