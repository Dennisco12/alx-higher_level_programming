#!/usr/bin/python3

'''This creates a class that defines a node'''


class Node:
    '''This is the class definition'''

    def __init__(self, data, next_node=None):
        '''This initialise the node'''

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''This is a private instance attribute to get the data'''

        return self.__data

    @data.setter
    def data(self, value):
        '''This is a property that sets the data'''

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''This is a getter to retrieve the next node'''

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''This sets the value of the next node'''

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''This defines the class for singly linked lists'''

    def __init__(self):
        '''This initialises the class'''
        self.__head = None

    def sorted_insert(self, value):
        '''This inserts a new node into a sorted node
        Args:
            value (int): The value to be inserted into the node.'''
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        '''This enables the list to be printed'''
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
