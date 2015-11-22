from ExtendedEuclideanAlgorithm import xgcd
import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print(modinv(int(args[0]),int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: ModularInverse.py -p <a: Z> <b: +Z>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: ModularInverse.py -p <a: Z> <b: +Z>")
def modinv(a,m):
	if type(a) is not int or type(m) is not int:
		raise TypeError('Arguments must be integers')
	g,x,y = xgcd(a,m)
	return None if g != 1 else x % m
if __name__ == "__main__":
    main()