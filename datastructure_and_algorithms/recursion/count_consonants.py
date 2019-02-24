"""
Count consonants
"""
vowels = "aeiou"
def recursive_count(strr):
	if strr == '':
		return 0

	if strr[0].lower() not in  vowels and strr[0].isalpha()  :
		return 1 + recursive_count(strr[1:])
	else:
		return recursive_count(strr[1:])

def main():
	
	print(recursive_count("Hello"))

if __name__ == '__main__':
	main()