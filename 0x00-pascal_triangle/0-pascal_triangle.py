#!/usr/bin/python
from math import factorial
"""Pascal Triangle"""


def pascal_triangle(n):
    """
    returns a lists of integers
    representing the Pascal’s triangle
    """
    li = []
    for i in range(1, n+1):
        comp = []
        for j in range(i):
            comp.append(factorial(i-1) // (factorial(j) * factorial(i-1-j)))
        li.append(comp)
    return li
