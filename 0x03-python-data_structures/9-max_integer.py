#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) > 0:
        max = 0

        for index, value in enumerate(my_list):
            if value > max:
                max = value

        return max

    return None
