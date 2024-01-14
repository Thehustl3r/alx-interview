#!/usr/bin/env python3
"""
    Alogarithm that determine the boxes is openable.
"""


def canUnlockAll(boxes):
    """This function find if all boxes is unlockable"""
    n = len(boxes)
    key = [0]
    visited_box = [0]
    for i in range(n-1):
        if i in key:
            for value in boxes[i]:
                for val in boxes[value]:
                    key.append(val)
                key.append(value)
        else:
            return False
    return True
