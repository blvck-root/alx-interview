#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins: A list of coin denominations.
        total: The target amount to achieve.

    Returns:
        The minimum number of coins required, or -1 if it's not possible.
    """

    if total <= 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    coins.sort(reverse=True)
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
            if dp[amount] > total:
                return -1

    return dp[-1] if dp[-1] != float("inf") else -1
