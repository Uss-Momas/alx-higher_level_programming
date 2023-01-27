#!/usr/bin/python3
""" 3-say_my_name Module

Functions it contains:
    say_my_name: prints a name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name function

    Prints to the screen a full name

    Args:
        first_name: a string containing the first name
        last_name: a string containin the last name
            default value is empty string

    Returns:
        Nothing for now
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
