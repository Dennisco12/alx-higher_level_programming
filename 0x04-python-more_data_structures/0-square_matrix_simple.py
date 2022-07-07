#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''A function that returns the square of the inputted matrix'''

    new_matrix = []

    for i in matrix:
        new_matrix.append(list(map((lambda x : x * 2), i)))

    return new_matrix
