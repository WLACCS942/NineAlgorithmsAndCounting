from Helper import *
import math
import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 3:
					raise getopt.GetoptError('')
				print(modExpo(int(args[0]),[int(i) for i in (args[1].strip('[]')).split(',')],int(args[2])))
			elif(opt[0] == '-h'):
				print("usage: BinaryModularExponentiation.py -p <b: Z> <n: array of binary digits> <m: +Z>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: BinaryModularExponentiation.py -p <b: Z> <n: array of binary digits> <m: +Z>")
def modExpo(b,n,m):
	if type(b) is not int or not isPositiveInt(m):
		raise TypeError("1st argument must be an integer and 3rd must be a positive integer.")
	if any(i not in (0,1) for i in n):
		raise ValueError("2nd argument must be a binary sequence.")
	x = 1
	length = len(n) - 1
	power = b % m
	for j in range(length,-1,-1):
		if n[j] == 1:
			x = (x * power) % m
		power = (power ** 2) % m
	return x
if __name__ == "__main__":
    main()