#!/usr/bin/python3
""" Module Solving Lockboxes Problem"""


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked"""
    keys = set()
    keys.add(0)
    n = len(boxes)
    for i, box in enumerate(boxes):
        for com in box:
            if com not in keys and (com - 1) < n and com != i:
                keys.add(com)
    return n == len(keys)
