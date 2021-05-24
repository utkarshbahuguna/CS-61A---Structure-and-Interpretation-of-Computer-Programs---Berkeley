# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/guer01.pdf

"""
1.6 Consider an insect in an M by N grid.
The insect starts at the bottom left corner,(0, 0), and wants to end up at the top right corner(M-1, N-1).
The insect is only capable of moving right or up.
Write a function paths that takes a grid length and width and returns the number of different paths the insect can take from the start to the goal.
"""

def paths(m, n):
    """
    >>> paths(2, 2)
    2
    >>> paths(117, 1)
    1
    """
    if m == 1 and n == 1:
        return 1
    elif m < 1 or n < 1:
        return 0
    else:
        return paths(m-1, n) + paths(m, n-1)

"""
1.7 Write a procedure merge(s1, s2) which takes two sorted (smallest value first) lists
and returns a single list with all of the elements of the two lists, in ascending order. Use recursion.
"""
def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if not s1 or not s2:
        return s1 if not s2 else s2
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])


"""
1.8 Mario needs to jump over a sequence of Piranha plants, represented as a string of dashes (no plant) and P’s (plant!).
He only moves forward, and he can either step (move forward one place) or jump (move forward two places) from each position.
How many different ways can Mario traverse a level without stepping or jumping into a Piranha plant?
Assume that every level begins with a dash (where Mario starts) and ends with a dash (where Mario must end up).
"""

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps or jumps to reach the end of the level without ever landing in a Piranha plant.
    Assume that every level begins and ends with a dash.
    
    >>> mario_number('-P-P-')   # jump, jump
    1
    >>> mario_number('-P-P--')   # jump, jump, step
    1
    >>> mario_number('--P-P-')  # step, jump, jump
    1
    >>> mario_number('---P-P-') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number('-P-PP-')  # Mario cannot jump two plants
    0
    >>> mario_number('----')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('----P----')
    9
    >>> mario_number('---P----P-P---P--P-P----P-----P-')
    180
    """
	
    if len(level) == 1:
        return 1
    elif len(level) < 1 or level[0] == 'P':
    	return 0
    else:
    	return mario_number(level[1:]) + mario_number(level[2:])