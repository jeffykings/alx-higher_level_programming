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

    tmp_str = ""
    i = 0

    while i != len(text):
        if text[i] == "\\":
            i += 1
            continue

        tmp_str += text[i]

        if text[i] == "." or text[i] == "?" or text[i] == ":":
            tmp_str += "\n\n"
            i += 1

        i += 1
    print(tmp_str, end="")
