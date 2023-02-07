#!/usr/bin/python3
""" Module JSON string to OBject
"""


import json


def from_json_string(my_str):
    """Converts a JSON string into Object

    Args:
        my_str: the string to be converted
    Returns:
        An object represented by JSON string
    """
    json_obj = json.loads(my_str)
    return json_obj
