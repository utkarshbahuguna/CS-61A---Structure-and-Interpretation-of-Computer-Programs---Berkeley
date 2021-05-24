# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/guer00.pdf

# 2.3 Define a function, count_digits, which takes in an integer, n, and counts the numberof digits in that number.

def count_digits(n):
    '''
    >>> count_digits(4)
    1
    >>> count_digits(12345678)
    8
    >>> count_digits(0)
    0
    '''
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count


# 2.4 Define a function, count_matches, which takes in two integers n and m, and counts the number of digits that match.

def count_matches(n, m):
    '''
    >>> count_matches(10, 30)
    1
    >>> count_matches(12345, 23456)
    0
    >>> count_matches(121212, 123123)
    2
    >>> count_matches(111, 11)
    2
    >>> count_matches(101, 10) # no place matches
    0
    '''
    matches = 0
    while n and m:
        if n % 10 == m % 10:
            matches += 1
        n, m = n // 10, m // 10
    return matches

"""
4.5 Write make_skipper, which takes in a number n and outputs a function.
When this function takes in a number x, it prints out all the numbers between 0 and x, skipping every nth number
(meaning skip any value that is a multiple of n).
"""
def make_skipper(n):
    """
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def skip(x):
        for i in range(x+1):
            if i % 2 != 0:
                print(i)
    return skip


# 4.6 Write a function that takes in a function cond and a number n and prints numbers from 1 to n where calling cond on that number returns True.

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n+1):
        if cond(i):
            print(i)


"""
4.7 Write a function similar to keep_ints like before, but now it takes in a number n and returns a function that has one parameter cond.
The returned function prints out numbers from 1 to n where calling cond on that number returns True.
"""

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keep(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
    return keep