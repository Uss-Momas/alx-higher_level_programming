#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    """ Function that Saves a object to a file

    Args:
        my_obj: the object to be converted to string
        filename: the file to store the information

    Returns:
        Nothing
    """
    with open(filename, 'w', encoding="utf-8") as f:
        string_obj = json.dumps(my_obj)
        f.write(string_obj)
