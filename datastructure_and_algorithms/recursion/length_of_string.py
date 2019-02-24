"""
Calculate the length of the string
"""

def recursive_str_length(strr):
	if strr == '':
		return 0
	return 1 + recursive_str_length(strr[1:])

def main():
	print(recursive_str_length("Hello"))

if __name__ == '__main__':
	main()