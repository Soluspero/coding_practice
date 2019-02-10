import time

def test():
    n, q = input().strip().split()
    nlist = input().strip().split()
    for i in range(int(q)):
        x =  input().strip().split()
        if x[0] == '1':
            nlist[int(x[1])-1] = x[0]
        else:
             print("EVEN" if nlist[int(x[2])-1] == '0' else "ODD")

t1 = time.clock()
test()		
print(f"time taken {time.clock()-t1}")
	
# def test():

# 	buffersize = 100000
# 	with open("input.txt",buffering=2000000000) as f:
# 		n, q = f.readline().strip().split()
# 		nlist = f.readline().strip().split()
# 		count = int(q)
# 		bufferr  = f.readlines(buffersize)

# 		while len(bufferr) > 0:
# 			for x in bufferr:
# 				x =  x.strip().split()
# 				nlist[int(x[1])-1]= x[0] if x[0] == '1' else print("EVEN" if nlist[int(x[2])-1] == '0' else "ODD") 

# 			bufferr  = f.readlines(buffersize)
# 		print(nlist[427378])
	

# def main():
# 	t1 = time.clock()
# 	test()
# 	print(f"time taken {time.clock()-t1}")

# main()