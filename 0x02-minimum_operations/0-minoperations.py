#!/usr/bin/env python3
""" Minimum Operations """


def minOperations(n=0):
    """
    Descriptino: calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    Returns an integer
    If n is impossible to achieve, return 0
    """
    prim = findSmallestPrim(n)
    operatinos, chars = prim, prim

    if chars < n:
        toCopy = prim
        operatinos += 1

    while (chars < n):
        if (n / chars) == prim:
            if n - chars == prim:
                return operatinos + 1
            return operatinos + 2
        else:
            operatinos += 1
            chars += toCopy
    if chars == n:
        return operatinos
    else:
        return 0


def findSmallestPrim(n):
    """
    Custimizied prim factorizatino algorithm to find minimum one
    """
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            return (divisor)
        divisor += 1
    return divisor
