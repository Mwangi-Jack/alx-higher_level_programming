#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """This class defines all its methods"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """This method initializes the class"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method retrieves the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method retrieves the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the private attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """This method returns the rectangle perimeter"""

        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the
        rectangle with the character '#'.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([
            f'{self.print_symbol}' * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """This function detects  instance deletion"""

        type(self).number_of_instances -= 1

        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method compares rectangles"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        This method returns an instance of the Rectangle class
        with equal width and height
        """

        return Rectangle(size, size)
