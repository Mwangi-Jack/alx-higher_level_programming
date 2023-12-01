#!/usr/bin/python3

def print_list_integer(my_list=[]):
    list(map(lambda x: print(my_list[x]), range(len(my_list))))
    # for i in range(len(my_list)):
    #     print(my_list[i])
