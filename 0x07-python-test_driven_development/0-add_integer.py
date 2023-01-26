#!/usr/bin/python3
""" 0-add_integer module
Module containing the function that adds integers
"""


def add_integer(a, b=98):
    """
    Function that add's two integers

    Args:
        a: first number
        b: second number, default is 98

    Returns:
        the addition of a,b : a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
