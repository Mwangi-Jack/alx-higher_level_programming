#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    for i in range(len(my_list)):
        truCount = 0
        for j in range(len(my_list)):
            if my_list[i] >= my_list[j]:
                truCount += 1

        if truCount == len(my_list):
            return my_list[i]
