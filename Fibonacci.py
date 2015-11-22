import sys, getopt

def main(): #main function that takes in command line arguments and passes them to core algorithm
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 1:
					raise getopt.GetoptError('')
				print("RESULT:",fib(int(args[0])))
			elif(opt[0] == '-h'):
				print("usage: Fibonacci.py -p <n: +Z >= 2>")
				print("-p: print output. Arguments MUST come after this switch.")
				print("-h: help")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: Fibonacci.py -p <n: +Z >= 2>")
		print("Use -h for help.")

def fib(n): #core algorithm
	if type(n) is not int or n < 2: 
		raise TypeError('Argument must be an integer greater or equal to 2')
	fib = lambda a,b,n: a if n == 0 else fib(b,b+a,n-1)
	return fib(0,1,n)

if __name__ == "__main__": #Invoke main when program is run
    main()