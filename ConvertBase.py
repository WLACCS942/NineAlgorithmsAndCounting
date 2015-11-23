from BaseExpansion import baseExpansion
from ToDecimal import toDecimal
import sys, getopt
from typing import *

def main(): #main function that takes in command line arguments and passes them to core algorithm
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 3:
					raise getopt.GetoptError('')
				print("RESULT:",convert([int(i) for i in (args[0].strip('[]')).split(',')],int(args[1]),int(args[2])))
			elif(opt[0] == '-h'):
				print("usage: ConvertBase.py -p <a: array of digits of base b> <old base b: +Z >= 2> <new base nb: +Z >= 2>")
				print("-p: print output. Arguments MUST come after this switch.")
				print("-h: help")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: ConvertBase.py -p <a: array of digits of base b> <base b: +Z >= 2> <new base nb: +Z >= 2>")
		print("Use -h for help.")

def convert(a: Sequence[int],b: int,nb: int) -> List[int]: #core algorithm
	return baseExpansion(toDecimal(a,b),nb) if nb != 10 else toDecimal(a,b)

if __name__ == "__main__": #Invoke main when program is run
    main() 