''' 
During the process of information gathering, we have to make sure that it is valid. Regex comes very handy in such tasks.
Here, we have few email addresses with us. You have to output only the valid email address.
Valid email addresses are composed of a username, domain name, and extension assembled in this 
format: username@domain.extension.
The username starts with an English alphabetical character, and any subsequent characters consist of one or 
more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.

Input Format
First line will contain an Integer, denoting the number of emails to validate.
Each of the next N lines will contain a string denoting the email address.

Constraints
1 <= N <= 50

Output Format
Output all the valid email address.
 '''

import re
import sys
def main():

 # Write code here 
 emailPattern=re.compile(r'^([a-zA-Z])(.)+@[a-zA-Z]+\.[a-zA-Z]{2,3}$')
 n = int(input())
 results =[]
 for _ in range(n):
     email = input()
     mo = emailPattern.search(email)
     if mo != None:
         results.append(mo.group())
 
 sys.stdout.write("\n".join(results))
     

main()





