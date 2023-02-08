#!/usr/bin/python3
"""My List Module
"""


class MyList(list):
    """ Class that inheritance everything from the
    list class
    """
    def __init__(self):
        """ Constructor of the MyList class
        """
        super().__init__()

    def print_sorted(self):
        """Sorts the list that was created
        sorted():
            - method that sorts an iterable and returns it without
            modifying the original one
        """
        print(sorted(self))
