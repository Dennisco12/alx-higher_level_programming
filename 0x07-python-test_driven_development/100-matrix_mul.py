#!/usr/bin/python3
"""A function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """This works on the principle of mathematical marix multiplication
        Argvs:
            m_a (list of lists): The contains the first matrix
            m_b (list of lists): This contains the second matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for items in m_a:
        if not isinstance(items, list):
            raise TypeError("m_a must be a list of lists")
    for items in m_b:
        if not isinstance(m_b, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for items in m_a:
        if len(items) == 0:
            raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for items in m_b:
        if len(items) == 0:
            raise ValueError("m_b can't be empty")
    for items in m_a:
        for elem in items:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for items in m_b:
        for elem in items:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    c = len(m_a[0])
    for items in m_a:
        if len(items) != c:
            raise TypeError("each row of m_a must be of the same size")
    d = len(m_b[0])
    for items in m_b:
        if len(items) != d:
            raise TypeError("each row of m_b must be of the same size")
    for item_a in m_a:
        if len(item_a) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    new_b = []
    p = 0
    row = []
    for items in range(len(m_b[0])):
        row = []
        for elem in range(len(m_b)):
            row.append(m_b[elem][items])
        new_b.append(row)

    for p in m_a:
        new_row = []
        for col in new_b:
            mul = 0
            for i in range(len(new_b[0])):
                mul += p[i] * col[i]
            new_row.append(mul)
        new_matrix.append(new_row)

    return new_matrix
