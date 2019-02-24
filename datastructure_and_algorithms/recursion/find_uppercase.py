"""
Find uppercase letter recursively
"""

def find_uppercase_recursive(strr,idx = 0):
	if strr[idx].isupper() :
		return strr[idx]
	
	if idx == len(strr) - 1:
		return "No uppercase letter found"

	return find_uppercase_recursive(strr,idx+1)

def main():
	
	print(find_uppercase_recursive("Hello"))

if __name__ == '__main__':
	main()