"""
Reverse string recursively
"""

def reverse(strr):
	if strr == '' :
		return strr
	return  reverse(strr[1:]) + strr[0]

def main():
	
	print(reverse("Hello"))

if __name__ == '__main__':
	main()