#!/usr/bin/python3

"""writes a string to a file"""


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8)

    Args:
        filename: its the file to be written into
        text: the string to be written in a file

    Return:
        the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
