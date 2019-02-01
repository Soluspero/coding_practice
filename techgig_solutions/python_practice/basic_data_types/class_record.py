import sys

def main():

 # Write code here
 summ = [0]*5
 marks = []
 t=int(input())
 
 for i in range(t):
   name, *marks = input().split()

   for m, x in enumerate(marks):
   		summ[m]+=int(x)

 for k in summ:
 	avg = float((k/(t*100))*100)
 	print("{:.2f}".format(avg), end=" ") # replace print with sys.stdout.write if needed.
    

main()

