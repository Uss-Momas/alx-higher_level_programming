#!/usr/bin/python3

class Node:
    """Class that defines the structure of a Node"""

    def __init__(self, data, next_node=None):
        """Initialize the Node class atributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter to the attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter to the attribute data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter to the next node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter to the next node attribute"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class that implements a linked list"""

    def __init__(self):
        """Initialize the list
        args:
            head (Node): the first Node of the list
        """
        self.__head = None

    def __str__(self):
        """The representation of the class as string"""
        temp = self.__head
        string = ""
        if temp is None:
            # list is empty
            return ""
        while temp is not None:
            if temp.next_node is None:
                break
            string += "{}\n".format(temp.data)
            temp = temp.next_node
        string += "{}".format(temp.data)
        return string

    def sorted_insert(self, value):
        """Inserts a new node in the right order
        args:
            value (int): is the data to be introduced
        """
        if self.__head is None:
            # list is empty
            self.__head = Node(value)
            return

        temp = self.__head
        if value < temp.data:
            self.__head = Node(value, self.__head)
            return
        next_n, prev = temp.next_node, temp
        while next_n is not None:
            # list has more than 1 element
            if value < next_n.data:
                prev.next_node = Node(value, next_n)
                return
            prev = next_n
            next_n = next_n.next_node
        prev.next_node = Node(value)
