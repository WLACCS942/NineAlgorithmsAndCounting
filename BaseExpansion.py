	import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print(baseExpansion(int(args[0]),int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: BaseExpansion.py -p <n: +Z> <base: +Z > 1>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: BaseExpansion.py -p <n: +Z> <base: +Z > 1>>")
def baseExpansion(n, base):
	if type(n) is not int or type(base) is not int or n < 0 or base < 0:
		raise Exception('Arguments must be positive integers')
	expansion = []
	while n != 0:
		expansion.insert(0,n % base)
		n = n // base
	return expansion
if __name__ == "__main__":
    main()