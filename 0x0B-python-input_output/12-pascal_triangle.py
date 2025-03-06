#!/usr/bin/python3

""" that returns a list of lists of integers representing the
    Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Pascal's triangle

    Args:
        n: size of the triangle

    Return: a list of lists of integers representing the Pascal’s
            triangle of n or an empty list if n <= 0
    """

    if n <= 0:
        return []

    pascal_list = [[1]]

    temp_list = list()

    for i in range(1, n):

        prev_row = pascal_list[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        pascal_list.append(new_row)

    return pascal_list
