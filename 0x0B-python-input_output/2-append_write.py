#!/usr/bin/python3

""" appends a string <F2>to a file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)

    Args:
        filename: it is the file we will edit or add string to
        text: string to be added

    Return: the number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
