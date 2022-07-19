#!/usr/bin/python3

class Square:
    def __init__(self, size):
        '''Size is a private attribute that is crucial for a square
        and the type and value must be controlled'''
        self.__size = size
