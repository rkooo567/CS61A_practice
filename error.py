try:
	x = 1 / 0 # Zero Division Error
except ZeroDivisionError as e:
	print('handling a', type(e))
	x = 0

print("x is renassigned as", x)

def invert(x):
	y = 1 / x
	print('Never printed if x is 0')
	return y

def invert_safe(x):
	try:
		invert(x)
	except ZeroDivisionError as e:
		print('handled', e)
		return 0
"""
invert_safe(1/0)
print("this is printed?")
"""

from operator import add, mul, truediv

def reduce(f, s, initial):
	"""
	f : a two argument function
	s : a sequence of values that ca nbe the second argument
	initial : a value that can be the first argument
	
	>>> reduce(mul, [2, 4, 8], 1)
	64
	>>> reduce(add, [1, 2, 3, 4], 0)
	10
	"""
	if not s:
		return initial
	else:
		first, rest = s[0], s[1:]
		return reduce(f, rest, f(initial, first))
def divide_all(n, ds):
	try:
		return reduce(truediv, ds, n)
	except ZeroDivisionError as e:
		return float("inf")