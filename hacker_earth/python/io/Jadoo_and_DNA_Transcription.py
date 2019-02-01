dna={'G':'C','C':'G','T':'A','A':'U',"no":"Invalid Input"}
inp = input()

#Solution 1
#sl = ""
# for x in inp:
#     if x in dna.keys():
#         sl+=dna[x]
#     else:
#         sl = dna['no']
#         break
#print(sl)

#Solution 2
sl = [dna[x] if x in dna.keys() else dna["no"]  for x in inp]
print("".join(sl) if dna["no"] not in sl else dna["no"])