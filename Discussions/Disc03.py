# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc03.pdf

# 1.1

def multiply(m, n):
    """ Multiply two numbers recursively.
    >>> multiply(5, 3)
    15
    """
    if n == 0 or m == 0:
        return 0
    else:
        return m + multiply(m, n-1)

"""
1.3 Recall the hailstone function from Homework 1. First, pick a positive integer n as the start.
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
Repeat this process until n is 1. Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
"""

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + hailstone(n // 2)
        else:
            return 1 + hailstone(3 * n + 1)

# 1.4 Implement the recursive is_prime function.

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(i):
        if i == 1:
            return 1
        return (1 if n % i == 0 else 0) + prime_helper(i-1)

    return prime_helper(n) == 2

"""
1.5 Write a procedure merge(n, m) which takes numbers with digits in decreasing order
Returns a single number with all of the digits of the two, in decreasing order.
Any number merged with 0 will be that number (treat 0 as having no digits). Use recursion.
"""

def merge(n, m):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n == 0 or m == 0:
       return max(n, m)
    elif n % 10 <= m % 10:
       return 10 * merge(n//10, m) + n % 10
    else:
       return 10 * merge(n, m//10) + m % 10

"""
1.6 Define a function make_fn_repeater which takes in a one-argument function f and an integer x.
It should return another function which takes in one argument, another integer.
This function returns the result of applying f to x this number of times. Use recursion.
"""
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    def repeat(n):
        if n == 0:
            return x
        else:
            return f(repeat(n-1))

    return repeat