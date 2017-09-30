def fibonacci(n):
	""" Return the nth fibonacci number using iteration

		n : nth fibonacci number
	>>> fibonacci(1)
	0
	>>> fibonacci(2)
	1
	>>> fibonacci(3)
	1
	>>> fibonacci(7)
	8
	"""
	prev, curr = 0, 1
	for i in range(2, n + 1):
		prev, curr = curr, prev + curr
	return prev