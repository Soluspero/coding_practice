''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here
 club1 = int(input())
 club1M = input().split() # set(input().split())
 club2 = int(input())
 club2M = input().split() # set(input().split())

 club1Set = set(club1M)
 club2Set = set(club2M)

 print(len(club1Set) + len(club2Set) - len(club1Set.intersection(club2Set)))
 # print(club2Set.union(club1Set))

main()

