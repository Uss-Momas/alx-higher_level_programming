#!/usr/bin/python3
"""Module 2-append_write"""


def append_write(filename="", text=""):
    """Functions that appends information in a file
    Args:
        filename: name of the file
        text: the text to append to the file
    Returns:
        number of chars written/added to the file
    """
    nb_chars = 0
    with open(filename, "a", encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
