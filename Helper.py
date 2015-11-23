#Helper module used by other files
from typing import *

typeList = [int, float]

def matchNumberArraySizes(a: Sequence[int],b: Sequence[int]) -> Tuple[Sequence[int], Sequence[int], int]:
	if any(type(i) not in typeList for i in a) or any(type(i) not in typeList for i in b):
		raise TypeError("Not a list of numbers.")
	if len(a) > len(b):
		length = len(a)
		b = [0] * (length - len(b)) + b
	else:
		length = len(b)
		a = [0] * (length - len(a)) + a
	return a,b,length
def isPositiveInt(a: Any) -> bool:
	return True if type(a) is int and a > 0 else False
def isNegativeInt(a: Any) -> bool:
	return True if type(a) is int and a < 0 else False
def isStrictDecreasing(a: Sequence[int]) -> bool:
	if any(type(i) not in typeList for i in a):
		raise TypeError("Not a list of numbers.")
	sI = True
	for i in range(0,len(a)-1):
		if a[i] < a[i+1]:
			sI = False
			break
	return sI