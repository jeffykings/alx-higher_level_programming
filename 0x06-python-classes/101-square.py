#!/usr/bin/python3

""" This contains a class Square"""


class Square:
    """Initiates the size of a class"""

    def __init__(self, size=0, position=(0, 0)):
        """Runs a class is called to initiate a class"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ setter for position"""

        if (not isinstance(value, tuple)) or len(value) != 2 or not \
                all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""

        print(self.__str__())

    def __str__(self):
        if self.__size == 0:
            return ""

        squared_v = "\n" * self.__position[1]

        for i in range(self.__size):
            squared_v += " " * self.__position[0]
            squared_v += "#" * self.__size + "\n"

        return squared_v.rstrip()
