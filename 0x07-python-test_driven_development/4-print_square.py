#!/usr/bin/python3
""" 4-print_square Module
Module that contains the function to print a square
"""


def print_square(size):
    """function print_square
    Prints a square to the stdout acordingly to a size

    Args:
        size: is the size/length of the square

    Returns:
        Nothing, just printing to the screen
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
