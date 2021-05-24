# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc01.pdf

def wears_jacket(temp, raining):
    """Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.

    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """

    return temp < 60 or raining


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True