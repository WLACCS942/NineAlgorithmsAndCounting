import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print(xgcd(int(args[0]),int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: ExtendedEuclideanAlgorithm.py -p <a: Z> <b: Z>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: ExtendedEuclideanAlgorithm.py -p <a: Z> <b: Z>")
def xgcd(a,b):
	if type(a) is not int or type(b) is not int:
		raise TypeError('Arguments must be integers')
	return __xgcdBody(a,b)
def __xgcdBody(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = xgcd(b % a,a)
        return (g, x - (b // a) * y, y)
if __name__ == "__main__":
    main()