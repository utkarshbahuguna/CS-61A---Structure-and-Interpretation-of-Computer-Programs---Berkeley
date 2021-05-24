# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc05.pdf

# 1.1

def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return 1 + max(height(b) for b in branches(t))

def square_tree(t):
    """Return a new tree with the square of every element in t.
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """

    return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])


"""
1.3 Write a function that takes in a tree and a value x
and returns a list containing the nodes along the path required to get from the root of the tree to a node containing x.
If x is not present in the tree, return None. Assume that the entries of the tree are unique.
"""
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    """
    if label(tree) == x:
        return [label(tree)]
    else:
        path = [find_path(b, x) for b in branches(tree) if find_path(b, x) != None]
        if path:
            return [label(tree)] + path[0]


"""
2.2 Write a function that takes in a value x, a value el, and a list and adds as many el’s to the end of the list as there are x’s.
Make sure to modify the original list using list mutation techniques.
"""

def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    lst.extend([el]*len([a for a in lst if a == x]))

def group_by(s, fn):
    """Takes in a sequence s and a function fn and returns a dictionary.

    The values of the dictionary are lists of elements from s.
    Each element e in a list should be constructed such that fn(e) is the same for all elements in that list.
    Finally, the key for each value should be fn(e).

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    grouped = {}
    for x in s:
        y = fn(x)
        if y not in grouped:
            grouped[y] = [x]
        else:
            grouped[y].append(x)
    
    sorted_dict = {}
    for key in sorted(grouped):
        sorted_dict[key] = grouped[key]
    
    return sorted_dict

"""
3.2 Write a function that takes in a number n and returns a one-argument function.
The returned function takes in a function that is used to update n. It should return the updated n.
"""
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def updater(fn):
       nonlocal n
       n = fn(n)
       return n
    return updater 


# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
