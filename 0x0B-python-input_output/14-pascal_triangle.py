#!/usr/bin/python3
"""Module with a function that returns a list of lists

    returns list of lists of integers representing the Pascal’s triangle of n
    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
    pt = []
    if n <= 0:
        return []
    if n == 1:
        return [1]
    for i in range(1, n + 1):
        num = 1
        row = []
        for j in range(1, i + 1):
            row += [num]
            num = num * (i - j) // j
        pt += [row]
    return pt
