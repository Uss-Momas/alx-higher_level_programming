#!/usr/bin/python3
""" is same class Module
"""


def is_same_class(obj, a_class):
    """ Verifies if an obj is a instance of a certain class
    Args:
        obj: the object
        a_class: the class to compare
    Returns:
        boolean: True or False
    """
    return isinstance(obj, a_class)
