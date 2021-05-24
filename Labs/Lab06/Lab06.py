
def make_adder_inc(n):
    """Write a function which takes in an integer n and returns a one-argument function.
    This function should take in some value x and return n + x the first time it is called.
    The second time it is called it should return n + x + 1, then n + x + 2 the third time, and so on.
    
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    i = -1
    def adder_inc(x):
        nonlocal i
        i += 1
        return n + x + i
    return adder_inc
