from EuclideanAlgorithm import gcd
import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print(lcm(int(args[0]),int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: BaseExpansion.py -p <Z> <Z>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: BaseExpansion.py -p <Z> <Z>")
def lcm(a,b):
	if type(a) is not int or type(b) is not int:
		raise TypeError('Arguments must be integers')
	return (a * b) // gcd(a,b)
if __name__ == "__main__":
    main()