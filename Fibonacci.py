import sys, getopt
def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 1:
					raise getopt.GetoptError('')
				print(fib(int(args[0])))
			elif(opt[0] == '-h'):
				print("usage: Fibonacci.py -p <+Z >= 2>")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: Fibonacci.py -p <+Z >= 2>")
def fib(n):
	if type(n) is not int or n < 2: 
		raise TypeError('Argument must be an integer greater or equal to 2')
	fib = lambda n: 0 if n == 0 else 1 if n == 1 else fib(n - 1) + fib(n - 2)
	return fib(n)
if __name__ == "__main__":
    main()