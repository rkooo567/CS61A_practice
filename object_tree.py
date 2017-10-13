# tree implementation using class

class Tree:
	def __init__(self, label, branches=[]):
		self.label = label
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)

	def __repr__(self):
		if self.branches:
			branch_str = ', ' + repr(self.branches)
		else:
			branch_str = ''
		return 'Tree({0}{1})'.format(self.label, branch_str)

	def __str__(self):
		return '\n'.join(self.indented())

	def indented(self, k=0):
		indented = []
		for b in self.branches:
			for line in b.indented(k + 1):
				indented.append('  ' + line)
		return [str(self.label)] + indented

	def is_leaf(self):
		return not self.branches

def memo(f):
	cache = {}
	def memorized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memorized

def leaves(tree):
	"""
	count the number of leaves in the tree
	>>> leaves([1, [1]])
	[1]
	>>> leaves([1, [1], [2]])
	[1, 2]
	>>> leaves(fib_tree(5))
	[1, 0, 1, 0, 1, 1, 0, 1]
	"""
	if tree.is_leaf():
		return [tree.label]
	else:
		return sum([leaves(branch) for branch in tree.branches], [])

def prune_repeats(t, seen):
	t.branches = [b for b in t.branches if b not in seen]
	seen.append(t)
	for b in t.branches:
		prune_repeats(b, seen)

# implement hailstone sequence by the tree class
def is_odd(n):
	return n % 2 == 1

def is_int(n):
	return int(n) == n

def can_triple_and_add_one(n):
	return n > 1 and is_odd(n) and is_int(n)

def hailstone_tree(k, n=1):
	""" hailstone seuquence by the tree class
	k : length
	n : the first value
	"""
	if k == 1:
		return Tree(n)
	else:
		up, down = 2 * n, (n - 1) / 3
		branches = [hailstone_tree(k - 1, up)]
		if can_triple_and_add_one(down):
			branches.append(hailstone_tree(k - 1, int(down)))
		return Tree(n, branches)

def paths(t):
	if t.is_leaf():
		return [ [t.label] ]
	else:
		result = []
		for b in t.branches:
			result.extend([[t.label] + p for p in paths(b)])
		return result