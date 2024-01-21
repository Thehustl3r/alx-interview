#!/usr/bin/python3
"""
0-minioperation
"""


from queue import Empty


def multiplesOfNum(n):
    """find multiples of number and store it in array"""
    mutlipes = []
    multi = 2
    while (n > 1):
        while (n % multi != 0):
            multi = multi+1
        mutlipes.append(multi)
        n = n / multi

    return mutlipes


def minOperations(n) -> int:
    """function that return minimal operation to create n times of H"""
    multiples = multiplesOfNum(n)
    num: int = 0
    while (len(multiples)):
        multi: int = multiples.pop()
        num = num + multi

    return num
