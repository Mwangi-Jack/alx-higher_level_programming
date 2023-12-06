#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_A = set_2.difference(set_1)
    set_B = set_1.difference(set_2)
    return set_A | set_B
