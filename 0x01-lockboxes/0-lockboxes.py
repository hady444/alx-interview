#!/usr/bin/python3
""" Module Solving Lockboxes Problem"""


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked"""
    keys = set([0])
    return recursive(0, boxes, keys)


def recursive(onKey, boxes, keys):
    """recursive functoion to help solving the problem"""
    for com in boxes[onKey]:
        if com not in keys com < len(boxes):
            keys.add(com)
            recursive(com, boxes, keys)
    return len(boxes) == len(keys)
