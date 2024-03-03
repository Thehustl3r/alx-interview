#!/usr/bin/python3
"""
0-making_change module
"""


def makeChange(coins, total):
    """
        The Program that find min number to reach target amount.
        Args:
            - coins: the list of available coins
            - total: the targeted amount to reach
        Return:
            - the minimun coins, otherwise -1
    """
    if total < 1:
        return 0
    number = 0
    prev_total = total
    coins = sorted(coins, reverse=True)
    while total > 0:
        prev_total = total
        for coin in coins:
            if (total - coin) >= 0:
                total -= coin
                number += 1
                break
        if total == prev_total:
            break
    if number == 0 or total != 0:
        return -1
    return number
