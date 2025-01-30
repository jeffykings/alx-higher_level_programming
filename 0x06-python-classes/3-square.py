#!/usr/bin/python3

""" This contains a class Square"""


class Square:
    """Initiates the size of a class"""

    def __init__(self, size=0):
        """Runs a class is called to initiate a class"""

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Returns the area of the square"""
        return (self.__size ** 2)
