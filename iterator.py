# implement for statement

def for_statement(iterable, f):
	items = iter(iterable)
	try:
		while True:
			item = next(items)
			f(item)
	# raised whenever next is called on an empty iterator
	except StopIteration:
		pass

def contains(a, b):
	a_i = iter(a)
	for x in b:
		try:
			while next(a_i) != x:
				pass
		except StopIteration:
			return False
	return True

def evens(start, end):
	even = start + (start % 2)
	while even < end:
		yield even
		even += 2

class Countdown(object):
	def __init__(self, number):
		self.number = number

	def count_down(self):
		number_iteration = iter(range(self.number, 0, -1))
		try:
			while True:
				print(next(number_iteration))
		except StopIteration:
			pass

	def __iter__(self):
		v = self.number
		while v > 0:
			yield v
			v -= 1

def a_then_b(a, b):
	for x in a:
		yield x
	for x in b:
		yield x

def a_then_b_simple(a, b):
	yield from a
	yield from b

def countdown(start):
	yield from range(start, 0, -1)

def countdown_2(k):
	if k > 0:
		yield k
		yield from countdown_2(k - 1)
	else:
		yield 'Blast off'

def prefixes(s):
	if s:
		yield from prefixes(s[:-1])
		yield s

def substrings(s):
	if s:
		yield from prefixes(s)
		yield from substrings(s[1:])