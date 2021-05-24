# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc04.pdf

"""
1.1 You want to go up a flight of stairs that has n steps. You can either take 1 or 2 steps each time.
How many different ways can you go up this flight of stairs? Write a function count_stair_ways that solves this problem. Assume n is positive.
"""

def count_stairways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stairways(n - 1) + count_stairways(n - 2)

"""
1.2 Consider a special version of the count_stairways problem, where instead of taking 1 or 2 steps, we are able to take up to and including k steps at a time.
Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive.
"""

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return sum(count_k(n - i, k) for i in range(1, k+1))


# 2.2

def even_weighted(lst):
    """Takes a list and returns a new list that keeps only the even-indexed elements of lst and multiplies them by their corresponding index.
    
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [lst[i] * i for i in range(len(lst)) if i % 2 == 0]

# 2.3

def max_product(lst):
    """Return the maximum product that can be formed using lst without using any consecutive numbers.
    
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not lst:
        return 1
    elif not lst[1:]:
        return lst[0]
    return max(max_product(lst[2:]) * lst[0], max_product(lst[3:]) * lst[1])