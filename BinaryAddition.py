from Helper import matchNumberArraySizes
import math
import sys, getopt
from typing import *

def main(): #main function that takes in command line arguments and passes them to core algorithm
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print("RESULT:",add([int(i) for i in (args[0].strip('[]')).split(',')],[int(i) for i in (args[1].strip('[]')).split(',')]))
			elif(opt[0] == '-h'):
				print("usage: BinaryAddition.py -p <a: sequence of binary digits> <b: sequence of binary digits>")
				print("-p: print output. Arguments MUST come after this switch.")
				print("-h: help")
	except (getopt.GetoptError, ValueError) as e:
		print("Error, usage is: BinaryAddition.py -p <a: sequence of binary digits> <b: sequence of binary digits>")
		print("Use -h for help.")
		
def add(a: Sequence[int],b: Sequence[int]) -> List[int]: #core algorithm
	if any(i not in (0,1) for i in a) or any(i not in (0,1) for i in b):
		raise ValueError("Arguments must be a sequence of binary digits.")
	a,b,length = matchNumberArraySizes(a,b)
	carry = 0
	s = [0] * length
	for j in range(length - 1,-1,-1):
		d = ( a[j] + b[j] + carry ) // 2 
		s[j] = a[j] + b[j] + carry - 2 * d
		carry = d
	if(carry == 1):
		s.insert(0,carry)
	return s

if __name__ == "__main__": #Invoke main when program is run
    main()