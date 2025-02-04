#!/usr/bin/python3
""" function that prints a square with the character #"""


def print_square(size):
    """ prints a square with the character #

    Args: 
        size: is the size length of the square must be an int

    Raises: 
        TypeError: if size is not an int
        ValueError: if size is less than 0
        TypeError: if size is a float and less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()

    else:
        for i in range(size):
            print("#" * size)
