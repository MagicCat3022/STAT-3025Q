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

def binomial_pmf(n: int, p: float, k: int) -> float:
    """Return the probability of getting exactly k successes in n independent Bernoulli trials with success probability p.

    Args:
        n (int): number of trials
        p (float): probability of success on each trial
        k (int): number of successes

    Returns:
        float: probability of getting exactly k successes
    """    
    if k > n or n < 0 or k < 0 or p < 0 or p > 1:
        raise ValueError("Invalid values for n, k, or p")
    
    return nCr(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomial_cdf(n: int, p: float, k: int) -> float:
    """Return the probability of getting at most (inclusive) k successes in n independent Bernoulli trials with success probability p.

    Args:
        n (int): number of trials
        p (float): probability of success on each trial
        k (int): number of successes

    Returns:
        float: probability of getting at most k successes
    """    
    if k > n or n < 0 or k < 0 or p < 0 or p > 1:
        raise ValueError("Invalid values for n, k, or p")
    
    total_prob = 0.0
    
    for i in range(k+1):
        total_prob += binomial_pmf(n, p, i)

    return total_prob

def geometric_pmf(p: float, k: int) -> float:
    """Return the probability of getting the first success on the (k+1)-th trial in a sequence of independent Bernoulli trials with success probability p.

    Args:
        p (float): probability of success on each trial
        k (int): number of failures before the first success

    Returns:
        float: probability of getting the first success on the (k+1)-th trial
    """    
    if k < 0 or p < 0 or p > 1:
        raise ValueError("Invalid values for k or p")
    
    return ((1 - p) ** (k - 1)) * p

def hypergeometric_pmf(N: int, M: int, n: int, k: int) -> float:
    """Return the probability of getting exactly k successes in n draws from a population of size N containing M successes, without replacement.

    Args:
        N (int): population size
        M (int): number of successes in the population
        n (int): number of draws
        k (int): number of observed successes

    Returns:
        float: probability of getting exactly k successes
    """    
    if n < 0 or k < 0 or n > N or k > M:
        raise ValueError("Invalid values for N, M, n, or k")

    return (nCr(M, k) * nCr(N - M, n - k)) / nCr(N, n)

def negative_binomial_pmf(r: int, p: float, k: int) -> float:
    """Return the probability of getting exactly k failures before the r-th success in a sequence of independent Bernoulli trials with success probability p.

    Args:
        r (int): number of successes
        p (float): probability of success on each trial
        k (int): number of failures

    Returns:
        float: probability of getting exactly k failures before the r-th success
    """    
    if r <= 0 or k < 0 or p < 0 or p > 1:
        raise ValueError("Invalid values for r, k, or p")
    
    return nCr(k + r - 1, r - 1) * (p ** r) * ((1 - p) ** k)