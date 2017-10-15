# Membership test
# Union
# Intersection
# Adjoin
# sets methods are not destructive

from Link import *

# As Linked List
def empty(s):
	return s is Link.empty

def contains(s, v):
	""" Return true if set s contains value v as an element"""
	if emtpy(s):
		return False
	elif s.first == v:
		return true
	else:
		return contains(s.rest, v)

def adjoin(s, v):
	if contais(s, v):
		return s
	else:
		return Link(v, s)

def intersect(set1, set2):
	"""
	big theta = n^2 -> inefficient
	"""
	in_set2 = lambda v: contains(set2, v)
	return filter_link(in_set2, set1)

def union(set1, set2):
	not_in_set_2 = lambda v: not contains(set2, v)
	set_1_not_set_2 = filter_link(not_in_set_2, set1)
	return extend_link(set_1_not_set_2, set2)

# ordered set : better efficiency 

def add(s, v):
	if s.first > v:
		s.first, s.rest = v, Link(s.first, s.rest)
	elif v == s.first:
		return 
	elif empty(s.rest):
		s.rest = Link(v)
	else:
		add(s.rest, v)

s = Link(1, Link(3, Link(5)))
