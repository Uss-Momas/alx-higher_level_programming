#!/usr/bin/python3
""" Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    Class that represents everything of a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of the Square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        part1 = "[{}] ({}) ".format(type(self).__name__, self.id)
        part2 = "{}/{} - {}".format(self.x, self.y, self.width)
        return part1 + part2

    # Getters and Setters
    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the Square"""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Dictionary representation of the object Square
        """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

    # GENERAL PUPORSE METHODS
    def update(self, *args, **kwargs):
        """Function that updates the values of the object
        """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 4:
                self.id, self.size, self.x, self.y = args
        else:
            for key in kwargs:
                if key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]
                elif key == "id":
                    self.id = kwargs[key]
