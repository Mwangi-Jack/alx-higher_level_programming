#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    new_my_list = list(set(my_list))

    for i in range(len(new_my_list)):
        total += new_my_list[i]

    return total
