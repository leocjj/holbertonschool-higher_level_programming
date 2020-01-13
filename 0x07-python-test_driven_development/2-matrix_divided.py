#!/usr/bin/python3
"""This module divides all elements of a matrix.

    matrix must be a list of lists of integers or floats
        otherwise raise a TypeError exception
        'matrix must be a matrix (list of lists) of integers/floats'

    Each row of the matrix must be of the same size
        otherwise raise a TypeError exception
        'Each row of the matrix must have the same size'

    div must be a number (integer or float)
        otherwise raise a TypeError exception
        'div must be a number'

    div can’t be equal to 0
        otherwise raise a ZeroDivisionError exception
        'division by zero'

    All elements of the matrix should be divided by div
        rounded to 2 decimal places

    Returns a new matrix
    You are not allowed to import any module

    This module supplies one function, matrix_divided(matrix, div).

    For example,

    >>> matrix_divided([[1, 2][3, 4]], 2)
    [[0.5, 1][1.5, 2]]
"""


def matrix_divided(matrix, div):
    """Return a new matrix dividing the original into div.

    Args:
        matrix: list of lists of integers or floats.
        div: divider, integer or float.

    Returns:
        list: list of lists of integers or floats.

    >>> matrix_divided([[1, 2]], 2)
    [[0.5, 1]]

    """

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/'
                        'floats')

    if len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/'
                        'floats')

    for item in matrix:
        if type(item) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of '
                            'integers/floats')

    if len(matrix[0]) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/'
                        'floats')

    for i in matrix:
        for j in i:
            if (type(j) is not float) and (type(j) is not int):
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')

    if (type(div) is not float) and (type(div) is not int):
        raise TypeError('div must be a number')

    if (float(div) is float('nan')) and (float(div) is float('inf')):
        raise TypeError('div must be a number')

    if (div is 0):
        raise ZeroDivisionError('division by zero')

    rows_ = len(matrix)
    len_row_ = len(matrix[0])

    for row in matrix:
        if len(row) != len_row_:
            raise TypeError('Each row of the matrix must have the same size')

    result_row_ = []
    result_matrix_ = []

    for row in matrix:
        for e in row:
            result_row_ += [round(e / div, 2)]
        result_matrix_ += [result_row_]
        result_row_ = []

    return result_matrix_
