#!/usr/bin/python3

"""function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    Raise:
        TypeError: if matrix is not a (list of lists) of integers/floats
        TypeError: if Each row of the matrix doesnt have the same size
        TypeError: if div is zero or not float or int
    """
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
        )

    new_matrix = []
    i = 0
    for row in matrix:
        temp_row = []

        if not isinstance(row, list):
            raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
            )
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        i += 1

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                        "matrix must be a matrix (list of lists) of "
                        "integers/floats"
                )

            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")

            if div == 0:
                raise ZeroDivisionError("division by zero")

            result = round(element / div, 2)
            temp_row.append(result)

        new_matrix.append(temp_row)

    return new_matrix
