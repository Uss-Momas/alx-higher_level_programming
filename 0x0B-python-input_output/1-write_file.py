#!/usr/bin/python3
""" Module with functions to write to file's
"""


def write_file(filename="", text=""):
    """ Function to write information to a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
