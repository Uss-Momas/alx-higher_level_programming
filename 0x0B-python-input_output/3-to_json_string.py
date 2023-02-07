#!/usr/bin/python3
""""Module 3-to_json_string"""


import json


def to_json_string(my_obj):
    """Function that returns JSON representation of an object(string)
    Returns the representation of JSON as a string
    """
    string_json = json.dumps(my_obj)
    return string_json
