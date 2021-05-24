""" Lab 07: Generators, Linked Lists, and Trees """
# https://inst.eecs.berkeley.edu/~cs61a/fa19/lab/lab07/

# Generators
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def scale(s, k):
    """A generator function which yields elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    
    # for i in s:
    #     yield k * i

    yield from map(lambda x: x * k, s)

# Linked Lists

def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.
    Assume that the input list is shallow; none of the elements is another linked list.
    Try to find both an iterative and recursive solution.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """

    # Iterative Solution
    """
    linked_to_list = []
    if link == Link.empty:
        pass
    else:
        link = Link(link.first, link.rest)
    
        while link is not Link.empty:
            linked_to_list.append(link.first)
            link = link.rest

    return linked_to_list
    """

    # Recursive Solution

    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)     

# Trees

def cumulative_sum(t):
    """Mutates t so that each node's label becomes the sum of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
        return t

    for branch in t.branches:
        cumulative_sum(branch)
        t.label += branch.label


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid Binary Search Tree (BST).

    Properties of a BST:
   
    Each node has at most two children (a leaf is automatically a valid binary search tree)
    The children are valid binary search trees
    For every node, the entries in that node's left child are less than or equal to the label of the node
    For every node, the entries in that node's right child are greater than the label of the node

    Note that, if a node has only one child, that child could be considered either the left or right child.

    It may be helpful to write helper functions bst_min and bst_max that return the minimum and maximum,
    respectively, of a Tree if it is a valid binary search tree.


    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    True
    """
    
    if t.is_leaf():
        return True
    
    branch_count = len(t.branches)
    
    # checking for at max two children
    if branch_count > 2:
        return False

    # checking for all branches to be bst
    for i in range(branch_count):
        if not is_bst(t.branches[i]):
            return False
    
    # checking less than and greater than conditions;
    # assuming left child and right child are in that order in the tree implementation (doctest #3)
    if branch_count == 2:
        if t.branches[0].label <= t.label and t.branches[1].label > t.label:
            return True
    else:
        # only one child, will satisfy BST condition
        return True

    return False


def bst_min(t):
    """Retun the minimum label in a Binary Search Tree.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> bst_min(t1)
    1
    """

    assert is_bst(t)
    
    if t.is_leaf():
        return t.label

    if t.branches[0].label <= t.label:
        return bst_min(t.branches[0])
    else:
        return t.label


def bst_max(t):
    """Retun the maximum label in a Binary Search Tree.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> bst_max(t1)
    8
    """

    assert is_bst(t)
    
    if t.is_leaf():
        return t.label

    if len(t.branches) == 2:
        return bst_max(t.branches[1])
    else:
        if t.branches[0].label > t.label:
            return bst_max(t.branches[0])
        else:
            return t.label


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