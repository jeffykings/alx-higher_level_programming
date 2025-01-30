#!/usr/bin/python3

"""Define a class Node and SinglyLinkedList"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """initiates attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value
    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if not isinstance(value, Node) or value != None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = vlue


class SinglyLinkedList:
    """defines a singly linked list"""

    self.__head = Node()

    def __init__(self):
        pass


