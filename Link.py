# Linked List is either empty or a first value and the rest of the linked list

class Link(object):
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def is_empty(self):
		if self.first == Link.empty:
			return True
		else:
			return False

	def show_link(self):
		if self.rest == self.empty:
			return str(self.first) + " -> nothing"
		return str(self.first) + " -> " + self.rest.show_link()

	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i - 1]

	def __len__(self):
		return 1 + len(self.rest)

s = Link(3, Link(4, Link(5)))
square = lambda x: x * x
odd = lambda x: x % 2 == 1

def extend_link(s, t):
	if s is Link.empty:
		return t
	else:
		return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
	""" 
	apply function f to every element in the Linked List s
	"""
	if s is Link.empty:
		return Link.empty
	else:
		return Link(f(s.first), map_link(f, s.rest))

def filter_link(filter, s):
	""" Return a link with elements of s for which f returns True """
	if s is Link.empty:
		return s
	else:
		if filter(s.first):
			return Link(s.first, filter_link(filter, s.rest))
		else:
			return filter_link(filter, s.rest)

def join_link(s, seperator):
	""" Return a string of all elements in s seperated by seperator. """
	assert type(seperator) == str, "seperator should be the string type"
	if s.rest is Link.empty:
		return str(s.first)
	else:
		return str(s.first) + seperator + join_link(s.rest, seperator)

def partitions(n, m):
	""" Return a linked list of partitions of n & parts of up to m.
	Each partition is represented as a linked list
	"""
	if n == 0:
		return Link(Link.empty)
	elif n < 0 or m == 0:
		return Link.empty
	else:
		using_m = partitions(n - m, m)
		with_m = map_link(lambda p: Link(m, p), using_m)
		without_m = partitions(n , m - 1)
		return extend_link(with_m, without_m)

def print_partitions(n, m):
	links = partitions(n, m)
	lines = map_link(lambda line: join_link(line, ' + '), links)
	map_link(print, lines)





