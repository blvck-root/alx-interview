#!/usr/bin/python3
"""
Mock Interview Question:
In a textfile there is a single character H.
Your text editor can execute only two
operations in this file. Copy All and Paste.
Given a number n, write a method that calculates
the fewest number of operations needed to result in
n H characters in the file.

The number of operations is proportional to the sum
of prime factors of n.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations
    to produce n Hs, using Copy All and Paste only
    starting from a single H character.
    """
    i = 2
    tmp = n
    prime_factors = []

    if n < i:
        return 0

    while tmp > 1:
        while tmp % i == 0:
            prime_factors.append(i)
            tmp /= i
        i += 1

    return sum(prime_factors) if prime_factors else n
