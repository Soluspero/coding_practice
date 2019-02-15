''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
# import sys
# def main():

#  # Write code here 
#  n  = int(input().strip())
#  alist = [int(x) for x in input().strip().split()]
#  sm = int(input().strip())
#  count = 0
#  for i in range(n-1):
#     if (alist[i] + alist[i+1])==sm:
#         count+=1
#  sys.stdout.write(str(count))

# main()

import sys
def main():

 # Write code here 
 n  = int(input().strip())
 alist = [int(x) for x in input().strip().split()]
 sm = int(input().strip())
 count = 0
 s = set()
 for i in range(n):
    t = sm - alist[i]
    if (t >=0 and t in s):
        count+=1
    s.add(alist[i])
 sys.stdout.write(str(count))

main()



