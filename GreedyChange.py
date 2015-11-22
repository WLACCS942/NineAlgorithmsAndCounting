from Helper import *
import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print(greedyChange([int(i) for i in (args[0].strip('[]')).split(',')],int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: GreedyChange.py -p <array of strictly descending +Z> <^-Z>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: GreedyChange.py -p <array of strictly descending +Z> <^-Z>")
def greedyChange(c,n):
	if any(not isPositiveInt(i) for i in c) or isNegativeInt(n):
		raise TypeError("Coin array must have positive integers and n must be a non-negative integer.")
	if not isStrictDecreasing(c):
		raise ValueError("Coin denomination array must be strictly increasing.")
	r = len(c)
	d = [0] * r
	for i in range(0,r):
		while n >= c[i]:
			d[i] += 1
			n -= c[i]
	return d
if __name__ == "__main__":
    main()