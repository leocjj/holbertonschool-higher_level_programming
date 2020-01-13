#!/usr/bin/python3
"""This module multiplies 2 matrices:

    Prototype: def matrix_mul(m_a, m_b):

    m_a and m_b must be validated with these requirements in this order

        m_a and m_b must be an list of lists of integers or floats:
            if m_a or m_b is not a list:
                raise TypeError('m_a must be a list')
                      TypeError('m_b must be a list')

            if m_a or m_b is not a list of lists:
                raise TypeError('m_a must be a list of lists')
                      TypeError('m_b must be a list of lists')

            if m_a or m_b is empty (it means: = [] or = [[]]):
                raise ValueError('m_a can't be empty')
                      ValueError('m_b can't be empty')

            if one element of those list of lists is not an integer or a float:
                raise TypeError('m_a should contain only integers or floats')
                      TypeError('m_b should contain only integers or floats')

            if m_a or m_b is not a rectangle
            (all ‘rows’ should be of the same size):
                raise TypeError('each row of m_a must be of the same size')
                      TypeError('each row of m_b must be of the same size')

        If m_a and m_b can’t be multiplied:
            raise ValueError('m_a and m_b can't be multiplied')

    You are not allowed to import any module

    This module supplies one function, matrix_mul(m_a, m_b)

    For example,

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
"""


def matrix_mul(m_a, m_b):
    """Return a new matrix, multiplies 2 matrices.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        list: list of lists of integers or floats.

    >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    [[13, 16]]

    """

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for item in m_a:
        if type(item) is not list:
            raise TypeError('m_a must be a list of lists')
    for item in m_b:
        if type(item) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        for j in i:
            if (type(j) is not float) and (type(j) is not int):
                raise TypeError('m_a should contain only integers or floats')
    for i in m_b:
        for j in i:
            if (type(j) is not float) and (type(j) is not int):
                raise TypeError('m_b should contain only integers or floats')

    cols_m_a = len(m_a[0])
    cols_m_b = len(m_b[0])
    for row in m_a:
        if len(row) != cols_m_a:
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b:
        if len(row) != cols_m_b:
            raise TypeError('each row of m_b must be of the same size')

    rows_m_a = len(m_a)
    rows_m_b = len(m_b)
    if cols_m_a != rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result_row_ = []
    result_matrix_ = []
    sum_ = 0

    """Matrix of the appropriate size: row_m_a x cols_m_b"""
    for i in range(rows_m_a):
        for j in range(cols_m_b):
            sum_ = 0
            for k in range(cols_m_a):
                sum_ += (m_a[i][k]) * (m_b[k][j])
            result_row_ += [sum_]
        result_matrix_ += [result_row_]
        result_row_ = []

    return result_matrix_
