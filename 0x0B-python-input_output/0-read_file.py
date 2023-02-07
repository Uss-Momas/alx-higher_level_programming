#!/usr/bin/python3
"""Read_file module
contains function to read a file
"""


def read_file(filename=""):
    """function that reads a file object
    with UTF-8 encoding
    """
    with open(filename, "r", encoding="utf-8") as f:
        # print(f.read(), end="")
        for line in f:
            print(line, end="")
