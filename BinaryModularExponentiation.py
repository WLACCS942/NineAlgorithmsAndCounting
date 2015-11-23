from Helper import *
import math
import sys, getopt
from typing import *

def main(): #main function that takes in command line arguments and passes them to core algorithm
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 3:
					raise getopt.GetoptError('')
				print("RESULT:",modExpo(int(args[0]),[int(i) for i in (args[1].strip('[]')).split(',')],int(args[2])))
			elif(opt[0] == '-h'):
				print("usage: BinaryModularExponentiation.py -p <b: Z> <n: array of binary digits> <m: +Z>")
				print("-p: print output. Arguments MUST come after this switch.")
				print("-h: help")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: BinaryModularExponentiation.py -p <b: Z> <n: array of binary digits> <m: +Z>")
		print("Use -h for help.")
		
def modExpo(b: int,n: Sequence[int],m: int) -> int: #core algorithm
	if type(b) is not int or not isPositiveInt(m):
		raise TypeError("1st argument must be an integer and 3rd must be a positive integer.")
	if any(i not in (0,1) for i in n):
		raise ValueError("2nd argument must be a binary sequence.")
	x = 1
	end = len(n) - 1
	power = b % m
	for j in range(end,-1,-1):
		if n[j] == 1:
			x = (x * power) % m
		power = (power ** 2) % m
	return x

if __name__ == "__main__": #Invoke main when program is run
    main()