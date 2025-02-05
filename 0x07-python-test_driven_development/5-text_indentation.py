#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these
characters ':', '.' and '?' """


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters:
    ., ? and :

    Args:
        text - must be a string

    Raise:
        TypeError: if text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if i == 0:
            while text[i] == ' ':
                i += 1

        print(text[i], end="")

        if text[i] in ".:?":
            print("\n")
            i += 1

            while i < len(text) and text[i] == ' ':
                i += 1

            continue

        i += 1
