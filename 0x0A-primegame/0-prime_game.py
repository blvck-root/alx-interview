#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Determine the prime game winner"""
    mariaWinCount = 0
    benWinCount = 0

    for i in range(x):
        primes = SieveOfEratosthenes(nums[i])
        isMariaTurn = True
        while(True):
            if not primes:
                if isMariaTurn:
                    benWinCount += 1
                else:
                    mariaWinCount += 1
                break
            smallestPrime = primes.pop(0)
            isMariaTurn = not isMariaTurn

    if mariaWinCount > benWinCount:
        return "Maria"

    if mariaWinCount < benWinCount:
        return "Ben"

    return None


def SieveOfEratosthenes(n):
    """
    Python program to print all
    primes smaller than or equal to
    n using Sieve of Eratosthenes.
    """
    primes = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes
