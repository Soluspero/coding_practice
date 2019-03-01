def printPattern(n, i): 

    if (n < 1): 
        return

    if (i <= n): 
      
        print("* ", end = "") 
        printPattern(n, i + 1) 
      
    else: 
        print("") 
        printPattern(n-1, 1)

def main():
	printPattern(5, 1) 

if __name__ == '__main__':
	main()
