#!/usr/bin/python3
"""
    Alogarithm that determine the boxes is openable.
"""


def canUnlockAll(boxes):
    """This function find if all boxes is unlockable"""
    open_boxes = set([0])
    key_found = set(boxes[0])

    while key_found:
        box_to_be_opened = key_found.pop()
        if 0 <= box_to_be_opened < len(boxes) and \
                box_to_be_opened not in open_boxes:
            open_boxes.add(box_to_be_opened)
            key_found.update(boxes[box_to_be_opened])

    return len(open_boxes) == len(boxes)
