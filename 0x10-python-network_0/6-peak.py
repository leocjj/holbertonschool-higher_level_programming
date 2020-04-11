#!/usr/bin/python3
"""This module has a function that finds a peak in a list of unsorted integers.

    Prototype: def find_peak(list_of_integers):
    You are not allowed to import any module
    Your algorithm must have the lowest complexity
    6-peak.py must contain the function
    6-peak.txt must contain the complexity of your algorithm:
    O(log(n)), O(n), O(nlog(n)) or O(n2)
"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers: list of unsorted integers.

    Returns:
    int: peak of the list
    """
    l = list_of_integers
    size = len(l)

    if size == 0:
        return None
    if size == 1:
        return l[1]

    lo = 0
    hi = size - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if l[mid] <= l[mid + 1]:
            lo = mid + 1
        elif l[mid - 1] >= l[mid]:
            hi = mid - 1
        elif l[mid - 1] <= l[mid] and l[mid] >= l[mid + 1]:
            return l[mid]
    return l[lo]
