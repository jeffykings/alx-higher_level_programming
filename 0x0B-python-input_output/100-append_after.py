#!/usr/bin/python3

""" a function that inserts a line of text to a file, after each line
    containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ a function that inserts a line of text to a file, after each line
        containing a specific string

        Args:
            filename: the file to modify
            search_string: the string we are looking for
            new_string: the string we want to add
    """

    with open(filename,  encoding="utf-8") as file:

        lst_of_str = []
        for line in file:
            lst_of_str.append(line)

            if search_string in line:
                lst_of_str.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as file:
        for text in lst_of_str:
            file.write(text)
