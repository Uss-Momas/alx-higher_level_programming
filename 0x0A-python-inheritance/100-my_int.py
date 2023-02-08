#!/usr/bin/python3
"""my int Module"""


class MyInt(int):
    """MyInt class that inheritates from int class
    """
    def __init__(self, value):
        super().__init__()
        self.__value = value

    def __eq__(self, second):
        return int(self) != int(second)

    def __ne__(self, second):
        return int(self) == int(second)
