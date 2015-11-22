import sys, getopt

def main(): #main function that takes in command line arguments and passes them to core algorithm
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'hp')
		for opt in opts:
			if(opt[0] == '-p'):
				if len(args) != 2:
					raise getopt.GetoptError('')
				print("RESULT:",toDecimal([int(i) for i in (args[0].strip('[]')).split(',')],int(args[1])))
			elif(opt[0] == '-h'):
				print("usage: ToDecimal.py -p <a: array of digits of base b> <base b: +Z >= 2>")
				print("-p: print output. Arguments MUST come after this switch.")
				print("-h: help")
	except (getopt.GetoptError, ValueError):
		print("Error, usage is: ToDecimal.py -p <a: array of digits of base b> <base b: +Z >= 2>")
		print("Use -h for help.")

def toDecimal(a,b): #core algorithm. Note that this differs from the textbook version, because the textbook version is WAY too slow.
	if type(b) is not int or b < 2:
		raise TypeError('2nd argument must be +Z => 2.')
	if any(i // b != 0 for i in a): 
		raise TypeError('1st argument must be array of digits of base b = %d' % b)
	end = len(a) - 1
	k = 0
	sum = 0
	for i in range(end,-1,-1):
		sum += a[i] * (b ** k)
		k += 1
	return sum

if __name__ == "__main__": #Invoke main when program is run
    main()