""" Homework 1: Control """
# https://inst.eecs.berkeley.edu/~cs61a/fa19/hw/hw01/

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a**2 + b**2 + c**2 - min(a, b, c) ** 2

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    i = n - 1
    factor = i
    while i > 0:
        if n % i == 0:
            factor = i
            break
        i -= 1
    return factor

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

"""Despite the doctests above, the above function actually does not do the same thing as an if statement in all cases.
    To prove this fact, write functions c, t, and f such that with_if_statement prints the number 2, but with_if_function prints both 1 and 2.
    """

def with_if_statement():
    """    
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return False

def t():
    print(1)

def f():
    print(2)
    

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    Hailstone sequence generation:
    Pick a positive integer n as the start.
    If n is even, divide it by 2.
    If n is odd, multiply it by 3 and add 1.
    Continue this process until n is 1.


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
    length = 1
    while n > 1:
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        length += 1
        print (n)
    return length
