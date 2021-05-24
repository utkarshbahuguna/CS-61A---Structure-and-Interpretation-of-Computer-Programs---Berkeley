# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc07.pdf


"""
1.2 Write the function is_palindrome such that it works for any data type that implements the sequence interface.
Assume that the Link class has implemented the __len__ method and a __getitem__ method which takes in integers.
"""

from Labs.Lab07 import link_to_list


def is_palindrome(seq):
    """ Returns True if the sequence is a palindrome. A palindrome is a sequence that reads the same forwards as backwards
    
    >>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
    False
    >>> is_palindrome(["l", "i", "n", "k"])
    False
    >>> is_palindrome("link")
    False
    >>> is_palindrome(Link.empty)
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(Link("a", Link("v", Link("a"))))
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome("ava")
    True
    """
    i = 0
    length = len(seq)
    while i < length // 2:
        if seq[i] != seq[-(i+1)]:
            return False
        i += 1
    return True
        
"""
2.1 Write a function which takes in a linked list and returns the sum of all its elements.
Assume all elements are integers.
"""

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """

    if lnk is Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)

"""
2.2 Write a function that takes in a Python list of linked lists and multiplies them element-wise. It should return a new linked list.
If not all of the Link objects are of equal length, return a linked list whose length is that of the shortest linked list given.
You may assume the Link objects are shallow linked lists, and that lst_of_lnks contains at least one linked list.
"""

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    shortest_lnk_length = min(list(map(len, lst_of_lnks)))
    if shortest_lnk_length == 0:
        return Link.empty
    else:
        new_list = []
        prod = 1
        for lnk in lst_of_lnks:
            prod *= lnk.first
            new_list.append(lnk.rest)
        return Link(prod, multiply_lnks(new_list))


def filter_link(link, f):
    """Returns a generator which yields the values of link for which f returns True.

    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest
        
def filter_no_iter(link, f):
    """Above function but without iteration.

    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)


def sum_paths_gen(t):
    """Returns a generator which yields the sum of all the nodes from a path from the root of tree t to a leaf.

    >>> t1 = Tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    if t.is_leaf():
        yield t.label
    
    for b in t.branches:
        for sum_paths in sum_paths_gen(b):
            yield t.label + sum_paths



# Link List Class

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    >>> s = Link(5, Link(8, Link(7, Link(9))))
    >>> len(s)
    4
    >>> s[3]
    9
    >>> s[0]
    5
    >>> s[-1]
    9
    >>> s[-2]
    7
    >>> y = Link(1)
    >>> y[1]
    'Index out of bound.'
    >>> y[-1]
    1
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Implemented for questions in this module

    def __len__(self):
        if self is Link.empty:
            return 0
        else:
            return 1 + Link.__len__(self.rest)

    def __getitem__(self, i):
        if self is Link.empty:
            return "Index out of bound."
        elif i == 0:
            return self.first
        elif i > 0:
            return Link.__getitem__(self.rest, i - 1)
        else:
            return Link.__getitem__(self, (len(self) + i))

# Tree ADT

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()