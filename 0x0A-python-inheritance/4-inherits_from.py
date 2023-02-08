#!/usr/bin/python3
"""inherits from Module
"""


def inherits_from(obj, a_class):
    """ Verifies if the obj is a subclass of the a_class

    issubclass(Bool, Bool)-> should return false, but returns True
    So to overcome this I had to verify if the type of obj is same as a_class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
