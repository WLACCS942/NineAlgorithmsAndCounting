from Helper import *
import sys, getopt
from typing import *

def main(): #main function that takes in command line arguments and passes them to core algorithm
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print(greedyChange([int(i) for i in (args[0].strip('[]')).split(',')],int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: GreedyChange.py -p <sequence of strictly descending +Z> <n: ^-Z>")
				print("-p: print output. Arguments MUST come after this switch.")
				print("-h: help")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: GreedyChange.py -p <sequence of strictly descending +Z> <n: ^-Z>")
def greedyChange(c: Sequence[int],n: int) -> List[int]: #core algorithm.
	if any(not isPositiveInt(i) for i in c) or isNegativeInt(n):
		raise TypeError("Coin array must have positive integers and n must be a non-negative integer.")
	if not isStrictDecreasing(c):
		raise ValueError("Coin denomination sequence must be strictly increasing.")
	r = len(c)
	d = [0] * r
	for i in range(0,r):
		while n >= c[i]:
			d[i] += 1
			n -= c[i]
	return d

if __name__ == "__main__": #Invoke main when program is run
    main()