#!/usr/bin/python3
""" Student class Module
"""


class Student:
    """ Student class representing
    the Student information
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance
        """
        my_dict = {}
        is_list_strings = True
        if attrs is not None:
            for att in attrs:
                if type(att) is not str:
                    is_list_strings = False
                    break
            if is_list_strings:
                for key in attrs:
                    if self.__dict__.get(key):
                        my_dict[key] = self.__dict__[key]
            return my_dict
        else:
            return self.__dict__
