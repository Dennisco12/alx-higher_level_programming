#!/usr/bin/python3

def matrix_divided(matrix, div):
    """This function deivides a matrix by an
    integer
    Argvs:
        matrix: This is a list to be divided
        div: This is an int, the divisor
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                "(list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix "
                    "(list of lists) of integers/floats")
    for num in matrix:
        for elem in num:
            if type(elem) not in (int, float):
                raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    for n in matrix:
        for m in matrix:
            if len(n) != len(m):
                raise TypeError("Each row of matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), items)) for items in matrix])
