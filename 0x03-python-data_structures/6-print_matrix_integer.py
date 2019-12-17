#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    I, J = len(matrix), len(matrix[0])
    for i in range(I):
        for j in range(J):
            print('{:d}'.format(matrix[i][j]), end="")
            if j < J - 1:
                print(" ", end="")
        print()
