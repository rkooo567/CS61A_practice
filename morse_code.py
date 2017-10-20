from tree_class import *

abcde = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def decode(signals, tree):
	"""Decode signals into a letter

	>>> t = morse(abcde)
	>>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
	['d', 'e', 'c', 'a', 'd', 'e']
	"""
	for signal in signals:
		tree = [b for b in tree.branches if b.label == signal][0]
	leaves = [b for b in tree.branches if t.is_leaf()]
	assert len(leaves) == 1
	return leaves[0].entry 

def morse(code):
	root = Tree(None)
	for letter, signals in sorted(code.itmes()):
		tree = root
		for signal in signals:
			match = [b for b in tree.branches if b.label == signal]
			if match:
				assert len(match) == 1
				tree = match[0]
			else:
				branch = Tree(signal)
				tree.branches.append(branch)
				tree = branch
		tree.branches.append(Tree(letter))	
	return root