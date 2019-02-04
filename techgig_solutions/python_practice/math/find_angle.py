#find an hypotenuse side and its angle

import sys
import math

def main():
	ab = int(input())
	bc  = int(input())

	tan = bc//ab
	result  = round(math.degrees(math.atan(tan)))
	sys.stdout.write(str(result))

main()