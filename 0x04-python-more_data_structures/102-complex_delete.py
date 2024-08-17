#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    for i in range(len(a_dictionary)):
        if a_dictionary[i] == 'C':
            del a_dictionary[i]
        print(a_dictionary[i])

    result = map(lambda x: list(map(lambda y: print(x[y]), x)), a_dictionary)
    print(list(result))
