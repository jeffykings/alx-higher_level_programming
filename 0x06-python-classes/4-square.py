#!/usr/bin/python3

""" This contains a class Square"""


class Square:
    """Initiates the size of a class"""

    def __init__(self, size=0):
        """Runs a class is called to initiate a class"""

        self.__size = size

    @property
    def size(self):
        """getter for size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""

        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")

        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Returns the area of the square"""

        return (self.__size ** 2)
