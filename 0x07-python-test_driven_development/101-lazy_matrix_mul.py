#!/usr/bin/python3
""" function that multiplies 2 matrices:"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 matrices

    Args:
        m_a : must be a natrix ie list of list
        m_b: must be a mtix ie list of list

    Returns: the product of the array
    """

    return np.matmul(m_a, m_b)
