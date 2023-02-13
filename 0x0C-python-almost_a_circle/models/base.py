#!/usr/bin/python3
"""base Module"""

import json


class Base(object):
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class
        Args:
            id: the id of the Base class
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    # GENERAL PURPOSE METHODS
    # # Class methods
    @classmethod
    def create(cls, **dictionary):
        """function to create a new object with the values of the dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads json configuration from a file
        """
        instances_dictionary = []
        instances = []
        with open(cls.__name__ + ".json", 'r') as f:
            string = f.read()
            instances_dictionary = cls.from_json_string(string)
            for instance in instances_dictionary:
                instances.append(cls.create(**instance))
        return instances


    @classmethod
    def save_to_file(cls, list_objs):
        """Method that saves the string json into a file
        """
        if list_objs is None:
            j = "[]"
        else:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(cls.__name__ + ".json", "w") as f:
            f.write(j)

    # # Static methods
    @staticmethod
    def from_json_string(json_string):
        """Returning the list representation of the json string
        """
        if type(json_string) is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns json string representation of a object
        """
        return json.dumps(list_dictionaries)
