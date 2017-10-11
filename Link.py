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

a = Link(4, Link(3, Link(4)))