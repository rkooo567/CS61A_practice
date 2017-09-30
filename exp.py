def is_ascending(n):
    """Returns True if the digits of N are in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    """
    curr = n % 10
    while n >= 10:
    	n = n // 10
    	tens = n % 10
    	if curr > tens:
    		return False
    	else:
    		curr = n % 10
    return True

def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    >>> can_win (8)
    False
    >>> can_win (7)
    True
    """
    "*** YOUR CODE HERE ***"
    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new_state = number - action
        if not can_win ( new_state ):
            return True
        action += 1
    return False

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
    	return 0
    else:
    	return how_many_digit(n // 10, 10 - (n % 10)) + ten_pairs(n // 10)

def how_many_digit(n, digit):
	""" Return the numbers of digits
	>>> how_many_digit(5505, 5)
	3
	>>> how_many_digit(1, 1)
	1
	>>> how_many_digit(123123, 6)
	0
	>>> how_many_digit(123123, 3)
	2
	"""
	if n == 0:
		return 0
	elif n % 10 == digit:
		return 1 + how_many_digit(n // 10, digit)
	else:
		return how_many_digit(n // 10, digit)

def triangular_sum(n):
    """
    >>> t_sum = triangular_sum(5)
    1
    3
    6
    10
    15
    >>> t_sum
    35
    """
    "*** YOUR CODE HERE ***"
    def triangualr_num(x):
    	return (x + 1) * x // 2
    total = 0
    for i in range(1, n + 1):
    	total += triangualr_num(i)
    	print(triangualr_num(i))
    return total

def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True

    """
    "*** YOUR CODE HERE ***"
    if low0 < low1 < high0 or low0 < high1 < high0:
    	return True
    else:
    	return False

def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1


    """
    "*** YOUR CODE HERE ***"
    n = 1
    largest_square = 0
    while True:
    	if n ** 2 >= x:
    		largest_square = (n - 1) ** 2
    		break
    	n += 1
    return largest_square

def square(x):
	return x * x

def argentina(n):
	print(n)
	if n > 0:
		return lambda k: k(n + 1)
	else:
		return 1 / n

def germany(n):
	if n > 1:
		print('hallo')
	if argentina(n - 2) >= 0:
		print('bye')
	return argentina(n + 2)

two_thousand = lambda two: lambda k: k(4)(10)
print(two_thousand(7)(lambda four: lambda teen: 2000 + four + teen))