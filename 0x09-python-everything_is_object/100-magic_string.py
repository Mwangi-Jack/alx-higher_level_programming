#!/usr/bin/python3
"""Magic string"""


def magic_string():
    """
    This function returns a string
    times the number of times it is called
    """

    if not hasattr(magic_string, 'count'):
        magic_string.count = 0

    magic_string.count += 1

    return 'BestSchool, ' * (magic_string.count - 1) + 'BestSchool'
