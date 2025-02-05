#!/usr/bin/python3
""" function that multiplies 2 matrices:"""


def matrix_mul(m_a, m_b):
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

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    row_idx = 0
    
    if len(m_a[row_idx]) !=  len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(max(len(m_a), len(m_b))):
        row_a = m_a[i] if i < len(m_a) else []
        row_b = m_b[i] if i < len(m_b) else []

        if not isinstance(row_a, list):
            raise TypeError("m_a must be a list of lists")

        if not isinstance(row_b, list):
            raise TypeError("m_b must be a list of lists")

        if len(m_a[0]) != len(row_a):
            raise TypeError("each row of m_a must be of the same size")

        if len(m_b[0]) != len(row_b):
            raise TypeError("each row of m_b must be of the same size")

        temp_sum = 0
        col_idx = 0
        new_matrix = []

        while (col_idx < len(row_b)):

            row_idx = 0
            row_a_iter = iter(row_a)
            temp_matrix = []

            for element_a in row_a_iter:
                if not isinstance(element_a,  (int, float)):
                    raise TypeError("m_a should contain only integers or floats")

                if not isinstance(m_b[row_idx][col_idx], (int, float)):
                    raise TypeError("m_b should contain only integers or floats")

                temp_sum += element_a * m_b[row_idx][col_idx]
                temp_matrix.append(temp_sum)
                row_idx += 1

            new_matrix.append(temp_matrix)
            col_idx += 1

    return new_matrix

