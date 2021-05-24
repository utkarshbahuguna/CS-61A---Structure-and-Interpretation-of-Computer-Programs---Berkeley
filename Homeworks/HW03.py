# https://inst.eecs.berkeley.edu/~cs61a/fa19/hw/hw03/

# Questions

def num_sevens(n):
    """Recursive function which returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    """
    if not n:
        return 0
    return (1 if n % 10 == 7 else 0) + num_sevens(n // 10)

def pingpong(n):
    """Recursive function which returns the nth element of the ping-pong sequence.

    The ping-pong sequence counts up starting from 1 and is always either counting up or counting down.
    At element k, the direction switches if k is a multiple of 7 or contains the digit 7.

    >>> pingpong(1)
    1
    >>> pingpong(2)
    2
    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
   
    # Earlier Attempt - O(N**2)
    """
    def switches_till(n):
		if n == 1:
			return 0
		else:
			if num_sevens(n) > 0 or n % 7 == 0:
				return switches_till(n-1) + 1
			else:
				return switches_till(n-1) + 0
			
	if n == 1:
		return 1
	else:
		if switches_till(n-1) % 2 == 0:
			return pingpong(n-1) + 1
		else:
			return pingpong(n-1) - 1

    """

    # New Attempt - O(N)

    def pingpong_helper(x = 1, i = 1, increasing = True):
        if x == n:
            return i
        else:
            if x % 7 == 0 or num_sevens(x) > 0:
                return pingpong_helper(x + 1, i + (-1 if increasing else 1), not increasing)
            else:
                return pingpong_helper(x + 1, i + (1 if increasing else -1), increasing)

    return pingpong_helper()      


from math import log2, pow
def count_change(amount):
    """Recursive function to return the number of ways to make change for amount when denomination of every coin is a power of 2: 1-cent, 2-cent, 4-cent, etc.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partitions(amount, largest_demonination):
    	if amount == 0:
    		return 1
    	elif amount < 0 or largest_demonination <= 0:
    		return 0
    	else:
    		return count_partitions(amount - largest_demonination, largest_demonination) + count_partitions(amount, largest_demonination//2)

    largest_demonination = pow(2, int(log2(amount)))
    return count_partitions(amount, largest_demonination)

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    if not lst:
        return []
    elif type(lst) is not list:
        return [lst]
    else:
        return list(flatten(lst[0]) + flatten(lst[1:]))


# Extra Questions

# Towers of Hanoi

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return lambda n: (lambda f, n: f(f, n))(lambda rec, n : 1 if n == 1 else n * rec(rec, n-1), n)
