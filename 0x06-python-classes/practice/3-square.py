#!/usr/bin/python3

class Square:
    _size = 0

    def __init__(self, size=0):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size myst be >= 0")
        else:
            self._size = size

    def area(self):
        return self._size ** 2
