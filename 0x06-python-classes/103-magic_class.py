#!/usr/bin/pythton3

"""class Magic"""

import math

class MagicClass:
    """ contains method init, area and circumference"""

    def __init__(self, radius):
        if not isinstance(radius, int) or not isinstance(radius, float):
            raise TypeError("radius must be a number")

        self._MagicClass__radius = radius

    def area(self):
        """area of a circle"""

        return (math.pi * (self._MagicClass__radius ** 2))

    def circumference(self):
        """calculate circumference of a circle"""

        return (2 * math.pi * self._MagicClass__radius)
