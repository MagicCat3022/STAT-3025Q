import numpy as np
import math
import typing

def factorial(n: int) -> int:
    """Return n!

    Args:
        n (int): non-negative integer

    Returns:
        int: n!
    """    
    return math.factorial(n)

def nCr(n: int, r: int) -> int:
    """Return n choose r

    Args:
        n (int): non-negative integer
        r (int): non-negative integer, r <= n

    Returns:
        int: n choose r
    """    
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for n and r")
    return math.comb(n, r)

def nPr(n: int, r: int) -> int:
    """Return n permute r

    Args:
        n (int): non-negative integer
        r (int): non-negative integer, r <= n

    Returns:
        int: n permute r
    """    
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for n and r")
    return math.perm(n, r)