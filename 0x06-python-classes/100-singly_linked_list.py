#!/usr/bin/python3
"""Module to create classes for a singly linked list."""


class Node:
    """node class for a singly linked list."""

    def __init__(self, data, next_node=None):
        """init method."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter method for __data."""
        return self.__data

    @data.setter
    def data(self, value):
        """setter method for __data."""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """getter method for __next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """setter method for __next_node."""
        if type(node) != Node and node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = node


class SinglyLinkedList:
    """class for a singly linked list."""

    def __init__(self):
        """init method."""
        self.head = None

    def __str__(self):
        string = ''
        curr = self.head
        while curr:
            string += str(curr.data) + '\n'
            curr = curr.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """inset a node sorted method."""
        new_node = Node(value)
        curr = self.head
        if curr is None:
            self.head = new_node
            return
        if curr.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return
        while curr.next_node is not None:
            if curr.next_node.data > value:
                break
            curr = curr.next_node
        new_node.next_node = curr.next_node
        curr.next_node = new_node
        return
