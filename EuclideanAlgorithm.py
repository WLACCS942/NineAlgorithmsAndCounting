import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print(gcd(int(args[0]),int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: EuclideanAlgorithm.py -p <Z> <Z>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: EuclideanAlgorithm.py -p <Z> <Z>")
def gcd(a,b):
	if type(a) is not int or type(b) is not int:
		raise TypeError('Arguments must be integers')
	gcd.gcd = lambda a,b: gcd.gcd(b % a,a) if a != 0 else b
	return gcd.gcd(a,b)
if __name__ == "__main__":
    main()