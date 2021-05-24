"""Lab 1: Expressions and Control Structures"""
# https://inst.eecs.berkeley.edu/~cs61a/fa19/lab/lab01/

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    sum = 0
    while n > 0:
        last_digit, n = n % 10, n // 10
        sum += last_digit

    return sum


"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    fact = 1
    while k > 0:
        fact = fact * (n - k + 1)
        k -= 1
    return fact

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    last_digit = n % 10
    n = n // 10
    while n > 0:
        current_digit, n = n % 10, n // 10
        if last_digit == 8 and current_digit == last_digit:
            return True
        last_digit = current_digit
    return False


