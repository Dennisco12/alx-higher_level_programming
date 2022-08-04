#!/usr/bin/python3
"""A function that returns a list of lists of integers representing
the pascal's triangle"""


def pascal_triangle(n):
    """n is the integer representing the size of the triangle"""
    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1]]
    while len(triangle) < n:
        item = [1]
        last = triangle[-1]
        a = 0
        b = 1
        while b < len(last):
            c = last[a] + last[b]
            item.append(c)
            a += 1
            b += 1
        item.append(1)
        triangle.append(item)

    return triangle
