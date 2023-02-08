#!/usr/bin/python3
""" add attribute Module
"""


def add_attribute(obj, objname, value):
    """ Adds atribute to object class
    Args:
        obj: the object
        objname: object name
        value: the value to be added
    """

    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")

    setattr(obj, objname, value)
