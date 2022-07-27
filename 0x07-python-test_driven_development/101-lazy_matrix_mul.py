#!/usr/bin/python3
"""This calculates a matrix product using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This modules calculates the product of two matrices
    and return the result"""

    return np.matmul(m_a, m_b)
