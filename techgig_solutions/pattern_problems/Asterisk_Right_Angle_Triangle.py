"""
*
* *
* * *
* * * *
* * * * *
"""

import sys
def main():

 # Write code here 
 n = int(input().strip())
 for i in range(1,n+1):
    s = "* "*i
    sys.stdout.write(s.strip())
    if i < n:
        sys.stdout.write("\n")
 
main()