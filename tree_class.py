from object_tree import *
class BTree(Tree):
	empty = Tree(None)

	def __init__(self, label, left=empty, right=empty):
		Tree.__init__(self, label, [left, right])

	@property
	def left(self):
		return self.branches[0]

	@property
	def right(self):
		return self.branches[1]

	def is_leaf(self):
		return [self.left, self.right] == [BTree.empty] * 2

	def __repr__(self):
		if self.is_leaf():
			return 'BTree({0})'.format(self.label)
		elif self.right is BTree.empty:
			left = repr(self.left)
			return 'BTree({0}, {1})'.format(self.label, left)
		else:
			left, right = repr(self.left), repr(self.right)
			if self.left is BTree.empty:
				left = 'BTree.empty'
			template = 'BTree({0}, {1}, {2})'
			return template.format(self.label, left, right)

def fib_tree(n):
	if n == 0 or n == 1:
		return BTree(n)
	else:
		left = fib_tree(n - 2)
		right = fib_tree(n - 1)
		fib_n = left.label + right.label
		return BTree(fib_n, left, right)
# function that processes binary tree
def content(t):
	if t is BTree.empty:
		return []
	else:
		return contents(t.left) + [t.label] + contents(t.right)

def balanced_bst(s):
	if not s:
		return BTree.empty
	else:
		mid = len(s) // 2
		left = balanced_bst(s[:mid])
		right = balanced_bst(s[mid+1:])
		return BTree(s[mid], left, right)

def largest(t):
	if t.right is BTree.empty:
		return t.label
	else:
		return largest(t.right)

def second(t):
	if t.is_leaf():
		return None
	elif t.right is BTree.empty:
		return second(t.left)
	elif t.right.is_leaf():
		return t.label
	else:
		second(t.right)

def contain(s, v):
	if s is BTree.empty:
		return False
	elif s.label == v:
		return True
	elif s.label < v:
		return contains(s.right, v)
	elif s.label > v:
		return contains(s.left, v)

def adjoin(s, v):
	if s is BTree.empty:
		BTree(v)
	elif s.label < v:
		return BTree(s.label, s.left, adjoin(s.right, v))
	elif s.label > v:
		return BTree(s.label, adjoin(s.left, v), s.right)
	else:
		return s