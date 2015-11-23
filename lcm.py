from EuclideanAlgorithm import gcd
import sys, getopt
from typing import *

def main(): #main function that takes in command line arguments and passes them to core algorithm
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print("RESULT:",lcm(int(args[0]),int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: BaseExpansion.py <Z> <Z>.")
				print("-p: print output. Arguments MUST come after this switch.")
				print("-h: help")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: BaseExpansion.py <Z> <Z>")
		print("Use -h for help.")

def lcm(a: int,b: int) -> int: #core algorithm
	if type(a) is not int or type(b) is not int:
		raise TypeError('Arguments must be integers')
	return (a * b) // gcd(a,b)

if __name__ == "__main__": #Invoke main when program is run
    main()