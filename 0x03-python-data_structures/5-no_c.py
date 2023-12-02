#!/usr/bin/python3

def no_c(my_string):
    new_my_string = ''

    for index, value in enumerate(my_string):
        if value == 'C' or value == 'c':
            continue
        else:
            new_my_string += value

    return new_my_string
