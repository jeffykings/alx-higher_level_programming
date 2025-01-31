#!/usr/bin/python3

"""class Magic"""


import math


class MagicClass:
    """ contains method init, area and circumference"""

    def __init__(self, radius=0):

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """area of a circle"""

        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """calculate circumference of a circle"""

        return (2 * math.pi * self.__radius)
