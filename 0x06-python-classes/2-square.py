#!/usr/bin/python3

"""Defining class Square"""

class Square:

    def __init__(self, size=0):
        """ initializing the class

        Args:
            size (int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
