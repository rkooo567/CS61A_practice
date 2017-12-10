def perfect_squares():
	n = 1
	while True:
		yield n * n
		n += 1

def zip_generator(*iterables):
	iterators = [iter(iterable) for iterable in iterables]
	while True:
		yield [next(iterator) for iterator in iterators]

# experiment
z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])

def generate_subsets():
	subsets = [[]]
	n = 1
	while True:
		yield subsets
		subsets += [subset + [n] for subset in subsets]
		n += 1


# experiment
subsets = generate_subsets()
for _ in range(3):
	print(next(subsets))

def fset():
	items = lambda x: False
	def add(y):
		nonlocal items
		f = items
		items = lambda x: f(y) or x == y
		return f(y)
	return add, items

def gen_naturals():
	current = 0
	while True:
		yield current
		current += 1
gen = gen_naturals()

# combiner that combines two input iterators using a given combination function.
def combiner(iterable1, iterable2, combiner):
	while True:
		first_iter = next(iterable1)
		second_iter = next(iterable2)
		yield combiner(first_iter, second_iter)


# takes a list of iterators and yields items from all of them in order.
def gen_all_items(lst):
	for i in lst:
		yield from i

# returns all subsets of the positive inteegers from 1 to n.
def generate_subsets():
	result = [[]]
	i = 1
	while True:
		yield result
		result.extend([[i] + element for element in result])
		i += 1
