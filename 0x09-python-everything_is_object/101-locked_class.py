#!/usr/bin/python3
"""100-locked_class Module"""


class LockedClass:
    """Locked class name"""

    __slots__ = ["first_name"]

    def __init__(self):
        """The constructor of the class"""
        self.first_name = ""
