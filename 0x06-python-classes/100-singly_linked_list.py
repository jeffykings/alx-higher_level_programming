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
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initialize an empty singly linked list"""
        self.__head = None

    def __str__(self):

        """Returns a string representation of the linked list.
        Returns:
        str: The linked list as a string, with one node per line."""

        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
