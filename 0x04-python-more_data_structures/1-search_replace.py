#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def func(x):
        if x == search:
            x = replace

        return x

    return list(map(lambda x: func(x), my_list))
