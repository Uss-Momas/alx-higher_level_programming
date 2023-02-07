#!/usr/bin/python3
"""
Module containing scripts that adds arguments to Python list
"""


import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main(filename=""):
    """main function
    Entry point of our script
    """
    argv = sys.argv[1:]
    file_exists = os.path.exists(filename)
    if file_exists:
        argv = load_from_json_file(filename) + argv
    save_to_json_file(argv, filename)
    # save_to_json_file(argv, filename)


if __name__ == "__main__":
    main("add_item.json")
