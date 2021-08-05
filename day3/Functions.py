# help(round)

# help(round(-2.01))

# help(print)


def leastDifference(a, b, c):
    """ Return the smallest difference between 2 numbers
    among a b and c.
    >>> least_Difference(1,5,-5) 
    4 
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(diff1, diff2, diff3)


print(leastDifference(3, 4, 5), leastDifference(
    2313, 343, 3423))

help(leastDifference)

mystery = print()

print(type(mystery))

print(mystery)

# Printing with separator as [ ... ]
print(1212, 12, 12, 1, 21, 21, sep=' ... ')
