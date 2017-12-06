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