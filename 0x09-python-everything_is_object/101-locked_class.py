#!/usr/bin/python3
""" defines locked class."""


class LockedClass:
    """
    hat prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called
    first_name.
    """
    __slots__ = ["first_name"]
