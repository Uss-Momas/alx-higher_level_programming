#!/usr/bin/python3
"""6-Load_from_json_file Module"""


import json


def load_from_json_file(filename=""):
    """Loads information from a json_file
    and convert it to the specific object type
    Args:
        filename: filename of the json
    """
    with open(filename, 'r', encoding="utf-8") as f:
        json_file_content = f.read()
        # or simple json.load(f.name)
        return json.loads(json_file_content)
