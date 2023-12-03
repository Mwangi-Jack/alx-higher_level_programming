#!/usr/bin/python3

def max_integer(my_list=[]):

    if not my_list:
        return None

    max_val = 0

    for index, value in enumerate(my_list):
        if value >= max_val:
            max_val = value

    return max_val
