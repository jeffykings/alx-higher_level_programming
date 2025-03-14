#!/usr/bin/python3

"""Square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """to update the attributes

        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute

        **kwargs can be thought of as a double pointer to a dictionary:
        key/value (keyworded arguments)

        **kwargs must be skipped if *args exists and is not empty
        """
        if args:
            lst = ["id", "size", "x", "y"]
            i = 0

            for value in args:
                setattr(self, lst[i], value)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
