#!/usr/bin/python3

def add_atribute(obj, objname, value):
    """ Adds atribute to object class
    """

    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")

    setattr(obj, objname, value)

