#!/usr/bin/python3
"""Defines an integer addition function.

    args:
        a: int or float
        b: int or float """


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float. """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
