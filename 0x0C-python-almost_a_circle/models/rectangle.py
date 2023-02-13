#!/usr/bin/python3
"""rectangle Module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inheritates from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """String representation of the object"""
        part1 = "[{}] ({}) ".format(type(self).__name__, self.id)
        part2 = "{}/{} - {}/{}".format(self.x, self.y, self.width, self.height)
        return part1 + part2

    # GETTERS AND SETTERS
    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """The height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height property"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # GENERAL PURPOSE METHODS
    def area(self):
        """Computes the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """displays the rectangle with # format"""
        for i in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x, end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def to_dictionary(self):
        """Function that returns the dictionary
        representation of a rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def update(self, *args, **kwargs):
        """Function to update variables of the class

        Args:
            *args: the list of arguments
        Returns:
            nothing
        """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 3:
                self.id, self.width, self.height = args
            elif len(args) == 4:
                self.id, self.width, self.height, self.x = args
            elif len(args) == 5:
                self.id, self.width, self.height, self.x, self.y = args
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'width':
                    self.width = kwargs[key]
                elif key == 'height':
                    self.height = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]
