#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """This class defines all its methods"""

    def __init__(self, width=0, height=0):
        """This method initializes the class"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """This method returns the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the private attribute width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """This method returns the private attribute 'height'"""

        return self.__height

    @height.setter
    def height(self, value):
        "This method sets the height"

        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


