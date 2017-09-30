def divisors(n):
	return [1] + [x for x in range(2, n) if n % x == 0]

def width(area, height):
	assert area % height == 0
	return area // height

def perimeter(width, height):
	return (2 * width) + (2 * height)

def minimum_perimeter(area):
	heights = divisors(area)
	perimeters = [perimeter(width(area, h), h) for h in heights]
	return min(perimeters)

def palendrome(word):
	if word == '' or len(word) == 1:
		return True
	elif word[0] == word[-1]:
		return palendrome(word[1:-1])
	else:
		return False