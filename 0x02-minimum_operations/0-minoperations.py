#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n=0):
    """
    Descriptino: calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0
    H = 1
    toPaste = 0
    count = 0
    while H < n:
        if n % H == 0:
            count += 2
            toPaste = H
            H = 2 * H
        else:
            count += 1
            H += toPaste
    return count
