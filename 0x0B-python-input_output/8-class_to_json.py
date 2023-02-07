#!/usr/bin/python3
""" Class to Json Module
"""


def class_to_json(obj):
    """function that returns a dict
    description with simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__
