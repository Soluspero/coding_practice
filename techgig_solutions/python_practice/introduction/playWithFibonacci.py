
import sys

def main():
	inp = int(input())
	a, b = 0 ,1
	sL = ""
	for _ in range(inp):
		sL+= str(a) + " "
		a,b  = b, a+b

	sys.stdout.write(sL.strip())

if __name__ == '__main__':
	main()