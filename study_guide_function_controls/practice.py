# Q6: Distance

from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    "*** YOUR CODE HERE ***"
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    "*** YOUR CODE HERE ***"
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2) + pow((z2 - z1), 2))

def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75

    """
    "*** YOUR CODE HERE ***"
    sum = 1 / x + 1 / y
    return 2 / sum

    def multiadder ( n ):
		""" Return a function that takes N arguments , one at a time , and adds them .
		>>> f = multiadder (3)
		>>> f (5)(6)(7) # 5 + 6 + 7
		18
		>>> multiadder (1)(5)
		5
		>>> multiadder (2)(5)(6) # 5 + 6
		11
		>>> multiadder (4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
		26
		"""
		assert n > 0
		if n == 1:
			return lambda x : x
		else :
			return lambda a : lambda b : multiadder (n -1)( a + b )