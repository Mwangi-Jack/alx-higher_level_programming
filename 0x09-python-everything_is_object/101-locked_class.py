#!/usr/bin/python3
"""
Using __slot__ to prevent dynamic creation
of instance attributes
"""


class LockedClass:
    """LockedClass class definition """
    __slots__ = ['first_name']
