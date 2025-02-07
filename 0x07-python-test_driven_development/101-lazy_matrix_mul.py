#!/usr/bin/python3
import numpy as np

""" function that multiplies 2 matrices:"""


def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 matrices

    Args:
        m_a : must be a natrix ie list of list
        m_b: must be a mtix ie list of list

    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not  list of list
        ValueError: if m_a or m_b is empty
        TypeError: if elements are not int or float
        TypeError: if rows are not the same
        ValueError: if it can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    arr1 = np.array(m_a)
    arr2 = np.array(m_b)

    return arr1 @ arr2
