#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        max = 0

        for index, value in enumerate(my_list):
            if value > max:
                max = value

        return max

    return None
