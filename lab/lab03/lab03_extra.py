""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def is_prime_helper(n, m):
        if m == 1:
            return True
        elif n % m == 0 and m > 2:
            return False
        else:
            return is_prime_helper(n, m - 1)

    return is_prime_helper(n, n - 1)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def num_digits(n, m):
        """Returns the number of times m appears in a positive integer n.

        >>> ten_pair_helper(555, 5)
        3
        >>> ten_pair_helper(1234,6)
        0
        """
        if n < 10:
            if n == m:
                return 1
            else: 
                return 0
        else:
            return num_digits(n % 10, m) + num_digits(n // 10, m)

    if n == 0:
        return 0
    else:
        return num_digits(n // 10, 10 - n % 10) + ten_pairs(n // 10)

   