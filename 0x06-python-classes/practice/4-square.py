#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square.

			Args:
				size (int): size of the square
        """
        self.__size = size


    @property
    def size(self):
        """Get the current size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self._size = size


    def area(self):
        """Return the current area of the square"""
        return self._size ** 2
